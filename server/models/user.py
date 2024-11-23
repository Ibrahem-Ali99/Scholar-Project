from utils.db import get_db_connection

# User class
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password 

    def get_details(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }

    def change_password(self, new_password):
        self.password = new_password
        return "Password updated successfully"
    
# Admin
class Admin(User):
    def __init__(self, user_id, email, password):
        super().__init__(user_id, "Admin", email, password)

    def view_all_users(self, db_connection):
        cursor = db_connection.cursor()
        query = """
        SELECT 'Student' AS user_type, name, email FROM Student
        UNION ALL
        SELECT 'Teacher', name, email FROM Teacher
        UNION ALL
        SELECT 'Parent', '', email FROM Parent
        """
        cursor.execute(query)
        return cursor.fetchall()
    
    def view_hiring_requests(self, db_connection):
        cursor = db_connection.cursor()
        query = """
        SELECT request_id, teacher_name, request_status
        FROM Hiring_requests
        WHERE request_status = 'Pending'
        """
        cursor.execute(query)
        return cursor.fetchall()



# Student
class Student(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def enroll_in_course(self, course_id, enrollment_date, db_connection):
        cursor = db_connection.cursor()
        query = "INSERT INTO Enrollment (course_id, student_id, enrollment_date) VALUES (%s, %s, %s)"
        cursor.execute(query, (course_id, self.user_id, enrollment_date))
        db_connection.commit()
        return f"Student {self.name} enrolled in course {course_id}"

    def make_payment(self, course_id, amount, payment_date, db_connection):
        cursor = db_connection.cursor()
        query = "INSERT INTO Payment (student_id, course_id, amount, payment_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (self.user_id, course_id, amount, payment_date))
        db_connection.commit()
        return f"Payment of {amount} made for course {course_id}"

    def view_progress(self, db_connection):
        cursor = db_connection.cursor()
        query = """
        SELECT Course_assessment.title, Student_progress.status, Student_progress.score
        FROM Student_progress
        INNER JOIN Course_assessment ON Student_progress.assessment_id = Course_assessment.assessment_id
        WHERE Student_progress.student_id = %s
        """
        cursor.execute(query, (self.user_id,))
        return cursor.fetchall()
    
    def track_progress(self, course_id, db_connection):
        cursor = db_connection.cursor()
        query = """
        SELECT 
            COUNT(CASE WHEN status = 'completed' THEN 1 END) AS completed_tasks,
            COUNT(*) AS total_tasks
        FROM (
            SELECT 'session' AS task_type, completion_date, status 
            FROM Student_progress
            WHERE student_id = %s AND assessment_id IN (
                SELECT assessment_id 
                FROM Course_assessment 
                WHERE course_id = %s
            )
            UNION ALL
            SELECT 'material' AS task_type, post_date AS completion_date, 'completed' AS status 
            FROM Course_content 
            WHERE course_id = %s
        ) AS combined_tasks
        """
        cursor.execute(query, (self.user_id, course_id, course_id))
        progress = cursor.fetchone()
        if progress:
            completed = progress['completed_tasks']
            total = progress['total_tasks']
            percentage = (completed / total) * 100 if total else 0
            return f"Progress: {percentage:.2f}% ({completed}/{total} tasks completed)"
        return "No progress data available."

    def rate_course(self, course_id, rating, comment, db_connection):
        cursor = db_connection.cursor()
        query = """
        INSERT INTO Course_rating (rated_by, course_id, rating, comment)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (self.user_id, course_id, rating, comment))
        db_connection.commit()
        return f"Course {course_id} rated successfully with {rating}/5."
    
    def provide_feedback(self, course_id, feedback, db_connection):
        cursor = db_connection.cursor()
        query = """
        INSERT INTO Course_feedback (student_id, course_id, feedback)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (self.user_id, course_id, feedback))
        db_connection.commit()
        return f"Feedback for course {course_id} recorded successfully."



# Teacher
class Teacher(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def create_course(self, course_name, course_description, db_connection):
        cursor = db_connection.cursor()
        query = "INSERT INTO Course (course_name, course_description, teacher_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (course_name, course_description, self.user_id))
        db_connection.commit()
        return f"Course '{course_name}' created successfully"

    def add_course_content(self, course_id, title, content_type, post_date, db_connection):
        cursor = db_connection.cursor()
        query = """
        INSERT INTO Course_content (course_id, title, content_type, post_date)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (course_id, title, content_type, post_date))
        db_connection.commit()
        return f"Content '{title}' added to course {course_id}"

    def add_assessment(self, course_id, title, max_score, post_date, deadline, db_connection):
        cursor = db_connection.cursor()
        query = """
        INSERT INTO Course_assessment (course_id, title, max_score, post_date, deadline)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (course_id, title, max_score, post_date, deadline))
        db_connection.commit()
        return f"Assessment '{title}' added to course {course_id}"


# Parent
class Parent(User):
    def __init__(self, user_id, email, password, student_id):
        super().__init__(user_id, "Parent", email, password)
        self.student_id = student_id

    def view_student_progress(self, db_connection):
        cursor = db_connection.cursor()
        query = """
        SELECT Course_assessment.title, Student_progress.status, Student_progress.score
        FROM Student_progress
        INNER JOIN Course_assessment ON Student_progress.assessment_id = Course_assessment.assessment_id
        WHERE Student_progress.student_id = %s
        """
        cursor.execute(query, (self.student_id,))
        return cursor.fetchall()



