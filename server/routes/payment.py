from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
import os
from utils.db import db
from models import Course, Enrollment, Payment, Student

payment = Blueprint("payment", __name__)

# Get course details by ID
@payment.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if course:
        return jsonify({
            'course_id': course.course_id,
            'course_name': course.course_name,
            'description': course.course_description,
            'price': course.price,
            'image_url': course.image_url
        })
    return jsonify({'message': 'Course not found'}), 404

# Enroll a student in a course
@payment.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.get_json()
    course_id = data.get('course_id')
    student_id = data.get('student_id')

    course = Course.query.get(course_id)
    student = Student.query.get(student_id)

    if not course or not student:
        return jsonify({'message': 'Invalid course or student ID'}), 404

    enrollment = Enrollment(course_id=course_id, student_id=student_id, enrollment_date=db.func.current_date())
    db.session.add(enrollment)
    db.session.commit()

    return jsonify({'message': 'Enrollment successful', 'enrollment_id': enrollment.enrollment_id})


@payment.route('/process-payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    course_id = data.get('course_id')
    student_id = data.get('student_id')
    amount = data.get('amount')

    course = Course.query.get(course_id)
    student = Student.query.get(student_id)

    if not course or not student:
        return jsonify({'message': 'Invalid course or student ID'}), 404

    payment = Payment(course_id=course_id, student_id=student_id, amount=amount, payment_date=db.func.current_date())
    db.session.add(payment)
    db.session.commit()

    return jsonify({'message': 'Payment successful', 'payment_id': payment.payment_id})

