from datetime import datetime, timezone

student_id = 1
course_id = 2


def test_create_payment_success(client, mocker):
    with client.session_transaction() as session:
        session['user_id'] = student_id 

    mock_student = mocker.MagicMock(student_id=student_id)
    mock_course = mocker.MagicMock(course_id=course_id)
    mocker.patch('models.user.Student.query.get', return_value=mock_student)
    mocker.patch('models.course.Course.query.get', return_value=mock_course)
    mocker.patch('models.payment.Payment.query.filter_by', return_value=None) # no dupls
    mocker.patch('utils.db.db.session.add')
    mocker.patch('utils.db.db.session.commit')

    payload = {
        "course_id": course_id,
        "amount": "100.00",
        "card_last_four_digits": "1234",
        "card_month": "12",
        "card_year": str(datetime.now().year % 100 + 1),
        "card_cvv": "123"
    }
    response = client.post(f'/payment?student_id={student_id}', json=payload)

    assert response.status_code == 201
    assert response.json['message'] == "Payment successful"


def test_create_payment_missing_fields(client, mocker):
    with client.session_transaction() as session:
        session['user_id'] = student_id 
    payload = {
        "course_id": course_id,
    }
    response = client.post(f'/payment?student_id={student_id}', json=payload)

    assert response.status_code == 400
    assert "Missing fields" in response.json['error']


def test_get_payments_by_student_success(client, mocker):
    mock_payment = mocker.MagicMock(
        payment_id=1,
        course_id=course_id,
        amount=100.00,
        payment_date=datetime.now(timezone.utc),
        card_last_four_digits="1234"
    )
    mocker.patch('models.payment.Payment.query.filter_by', return_value=[mock_payment])
    response = client.get(f'/payment/student/{student_id}')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['course_id'] == course_id



def test_delete_payment_success(client, mocker):
    mock_payment = mocker.MagicMock(payment_id=1)
    mocker.patch('models.payment.Payment.query.get', return_value=mock_payment)
    delete_mock = mocker.patch('utils.db.db.session.delete')
    commit_mock = mocker.patch('utils.db.db.session.commit')
    response = client.delete('/payment/1')

    assert response.status_code == 200
    delete_mock.assert_called_once_with(mock_payment)
    commit_mock.assert_called_once()
    assert response.json['message'] == "Payment deleted successfully"

