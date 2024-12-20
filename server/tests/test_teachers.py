import pytest
from server.app import create_app
from server.models.user import Teacher
from server.utils.db import db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

@pytest.fixture
def sample_teacher():
    return {
        'name': 'Test Teacher',
        'email': 'test@teacher.com',
        'password': 'password123',
        'designation': 'Python Instructor'
    }

def test_create_teacher(client, sample_teacher):
    response = client.post('/api/teachers', json=sample_teacher)
    assert response.status_code == 201
    assert response.json['name'] == sample_teacher['name']
    assert response.json['email'] == sample_teacher['email']

def test_get_teacher(client, sample_teacher):
    # First create a teacher
    client.post('/api/teachers', json=sample_teacher)
    # Then retrieve the teacher
    response = client.get('/api/teachers/1')
    assert response.status_code == 200
    assert response.json['name'] == sample_teacher['name']

def test_update_teacher(client, sample_teacher):
    # Create teacher first
    client.post('/api/teachers', json=sample_teacher)
    # Update teacher
    update_data = {'designation': 'Senior Python Instructor'}
    response = client.put('/api/teachers/1', json=update_data)
    assert response.status_code == 200
    assert response.json['designation'] == update_data['designation']

def test_teacher_courses(client, sample_teacher):
    # Create teacher with courses
    client.post('/api/teachers', json=sample_teacher)
    response = client.get('/api/teachers/1/courses')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_teacher_dashboard_stats(client, sample_teacher):
    # Test dashboard statistics endpoints
    client.post('/api/teachers', json=sample_teacher)
    teacher_id = 1
    def test_teacher_search(client, sample_teacher):
        # Create teacher first
        client.post('/api/teachers', json=sample_teacher)
        
        # Test search by name
        response = client.get('/api/teachers/search?query=Test')
        assert response.status_code == 200
        assert isinstance(response.json, list)
        assert len(response.json) > 0

    def test_teacher_profile_update(client, sample_teacher):
        # Create teacher
        client.post('/api/teachers', json=sample_teacher)
        
        # Update profile
        profile_data = {
            'bio': 'Experienced Python instructor',
            'phone': '1234567890',
            'expertise': ['Python', 'Flask', 'Django']
        }
        response = client.patch('/api/teachers/1/profile', json=profile_data)
        assert response.status_code == 200
        assert response.json['bio'] == profile_data['bio']
        assert response.json['phone'] == profile_data['phone']

    def test_teacher_reviews(client, sample_teacher):
        # Create teacher
        client.post('/api/teachers', json=sample_teacher)
        
        # Get teacher reviews
        response = client.get('/api/teachers/1/reviews')
        assert response.status_code == 200
        assert isinstance(response.json, list)

    def test_teacher_availability(client, sample_teacher):
        # Create teacher
        client.post('/api/teachers', json=sample_teacher)
        
        # Set availability
        availability = {
            'monday': ['9:00-12:00', '14:00-17:00'],
            'tuesday': ['10:00-15:00']
        }
        response = client.post('/api/teachers/1/availability', json=availability)
        assert response.status_code == 200
        
        # Get availability
        response = client.get('/api/teachers/1/availability')
        assert response.status_code == 200
        assert 'monday' in response.json
        assert 'tuesday' in response.json

    def test_teacher_statistics(client, sample_teacher):
        # Create teacher
        client.post('/api/teachers', json=sample_teacher)
        
        # Get teaching stats
        response = client.get('/api/teachers/1/statistics')
        assert response.status_code == 200
        assert 'total_students' in response.json
        assert 'total_courses' in response.json
        assert 'average_rating' in response.json

