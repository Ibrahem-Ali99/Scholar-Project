from flask import Blueprint, request, jsonify, session
from utils.db import db
from models.payment import Payment
from models.user import Student
from models.course import Course
from datetime import datetime, timezone

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/payment', methods=['POST'])
def create_payment():
    print("Session details during payment:", dict(session))
    print("Cookies received:", request.cookies)
    print("Request headers:", request.headers) 

    try:
        student_id = request.args.get('student_id', type=int)
        if not student_id:
            print("Missing student_id in query parameters")
            return jsonify({'error': 'Student ID is required'}), 400

        if session.get('user_id') != student_id:
            print("Session mismatch or user not logged in")
            return jsonify({'error': 'User not logged in or session mismatch'}), 401

        data = request.get_json()
        print("Received JSON data:", data)

        course_id = data.get('course_id')
        amount = data.get('amount')
        amount = float(amount)
        card_last_four = data.get('card_last_four_digits')
        card_month = data.get('card_month')
        card_year = data.get('card_year')
        card_cvv = data.get('card_cvv')

        missing_fields = [
            field for field, value in {
                'course_id': course_id,
                'amount': amount,
                'card_last_four_digits': card_last_four,
                'card_month': card_month,
                'card_year': card_year,
                'card_cvv': card_cvv,
            }.items() if not value
        ]
        if missing_fields:
            print("Missing fields:", missing_fields)
            return jsonify({'error': f"Missing fields: {', '.join(missing_fields)}"}), 400

        student = Student.query.get(student_id)
        course = Course.query.get(course_id)
        print("Student found:", student)
        print("Course found:", course)

        if not student:
            return jsonify({'error': 'Student not found'}), 404
        
        if not course:
            return jsonify({'error': 'Course not found'}), 404
        
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid payment amount:", amount)
            return jsonify({'error': 'Invalid payment amount'}), 400
        
        if len(card_last_four) != 4 or not card_last_four.isdigit():
            print("Invalid card last four digits:", card_last_four) 
            return jsonify({'error': 'Invalid card last four digits'}), 400
        
        if not (1 <= int(card_month) <= 12):
            print("Invalid card month:", card_month) 
            return jsonify({'error': 'Invalid card month'}), 400
        
        current_year = datetime.now(timezone.utc).year % 100 # get last two digita of the year
        if not (int(card_year) >= current_year):
            print("Invalid card year:", card_year)
            return jsonify({'error': 'Invalid card year'}), 400
        
        if len(card_cvv) != 3 or not card_cvv.isdigit():
            print("Invalid card CVV:", card_cvv) 
            return jsonify({'error': 'Invalid card CVV'}), 400

        payment = Payment(
            student_id=student_id,
            course_id=course_id,
            amount=amount,
            payment_date=datetime.utcnow(),
            card_last_four_digits=card_last_four,
            card_month=int(card_month),
            card_year=int(card_year),
            card_cvv=card_cvv
        )
        db.session.add(payment)
        db.session.commit()
        print("Payment successful:", payment.payment_id) 
        return jsonify({'message': 'Payment successful', 'payment_id': payment.payment_id}), 201
    except Exception as e:
        db.session.rollback()
        print("Unexpected error:", str(e))
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500



@payment_bp.route('/payment/student/<int:student_id>', methods=['GET'])  
def get_payments_by_student(student_id):
    try:
        payments = Payment.query.filter_by(student_id=student_id).all()

        if not payments:
            return jsonify({'message': 'No payments found for this student'}), 404

        result = [{
            'payment_id': p.payment_id,
            'course_id': p.course_id,
            'amount': p.amount,
            'payment_date': p.payment_date.strftime('%Y-%m-%d'),
            'card_last_four_digits': p.card_last_four_digits
        } for p in payments]

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@payment_bp.route('/payment/course/<int:course_id>', methods=['GET'])
def get_payments_by_course(course_id):
    try:
        payments = Payment.query.filter_by(course_id=course_id).all()

        if not payments:
            return jsonify({'message': 'No payments found for this course'}), 404

        result = [{
            'payment_id': p.payment_id,
            'student_id': p.student_id,
            'amount': p.amount,
            'payment_date': p.payment_date.strftime('%Y-%m-%d'),
            'card_last_four_digits': p.card_last_four_digits
        } for p in payments]

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@payment_bp.route('/payment', methods=['GET'])  
def get_all_payments():
    try:
        payments = Payment.query.all()

        if not payments:
            return jsonify({'message': 'No payments found'}), 404

        result = [{
            'payment_id': p.payment_id,
            'student_id': p.student_id,
            'course_id': p.course_id,
            'amount': p.amount,
            'payment_date': p.payment_date.strftime('%Y-%m-%d'),
            'card_last_four_digits': p.card_last_four_digits
        } for p in payments]

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@payment_bp.route('/payment/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    try:
        payment = Payment.query.get(payment_id)

        if not payment:
            return jsonify({'error': 'Payment not found'}), 404

        db.session.delete(payment)
        db.session.commit()

        return jsonify({'message': 'Payment deleted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@payment_bp.route('/api/admin/payment', methods=['GET'])  
def get_admin_payments():
    try:
        payments = db.session.query(
            Payment, Student, Course
        ).join(
            Student, Payment.student_id == Student.student_id
        ).join(
            Course, Payment.course_id == Course.course_id
        ).all()

        result = [{
            'payment_id': p.Payment.payment_id,
            'student_name': p.Student.name,
            'student_email': p.Student.email,
            'course_name': p.Course.course_name,
            'amount': float(p.Payment.amount),
            'payment_date': p.Payment.payment_date.strftime('%Y-%m-%d'),
            'card_last_four_digits': p.Payment.card_last_four_digits
        } for p in payments]

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
