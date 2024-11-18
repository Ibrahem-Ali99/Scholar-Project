-- Switch to the scholar database
USE scholar;

-- Insert data into Student table
INSERT INTO Student (name, password, email)
VALUES
('Alice Johnson', 'encrypted_password_1', 'alice@example.com'),
('Bob Smith', 'encrypted_password_2', 'bob@example.com'),
('Charlie Davis', 'encrypted_password_3', 'charlie@example.com');

-- Insert data into Teacher table
INSERT INTO Teacher (name, email, password)
VALUES
('Dr. Emily White', 'emily.white@example.com', 'encrypted_password_4'),
('Prof. John Brown', 'john.brown@example.com', 'encrypted_password_5');

-- Insert data into Course table
INSERT INTO Course (course_name, course_description, teacher_id)
VALUES
('Math 101', 'Introduction to Algebra', 1),
('Physics 202', 'Basics of Mechanics', 2);

-- Insert data into Parent table
INSERT INTO Parent (email, password, student_id)
VALUES
('parent1@example.com', 'encrypted_password_6', 1),
('parent2@example.com', 'encrypted_password_7', 2);

-- Insert data into Admin table
INSERT INTO Admin (email, password)
VALUES
('admin@example.com', 'encrypted_password_8');

-- Insert data into Enrollment table
INSERT INTO Enrollment (course_id, student_id, enrollment_date)
VALUES
(1, 1, '2024-01-15'),
(2, 2, '2024-01-16');

-- Insert data into Payment table
INSERT INTO Payment (student_id, course_id, amount, payment_date)
VALUES
(1, 1, 100.00, '2024-01-20'),
(2, 2, 150.00, '2024-01-22');

-- Insert data into Course_content table
INSERT INTO Course_content (course_id, title, content_type, post_date)
VALUES
(1, 'Algebra Basics', 'PDF', '2024-01-25'),
(2, 'Mechanics Overview', 'PowerPoint', '2024-01-27');

-- Insert data into Course_assessment table
INSERT INTO Course_assessment (course_id, title, max_score, post_date, deadline)
VALUES
(1, 'Algebra Quiz', 100, '2024-02-01', '2024-02-07'),
(2, 'Mechanics Exam', 100, '2024-02-02', '2024-02-08');

-- Insert data into Student_progress table
INSERT INTO Student_progress (student_id, assessment_id, status, completion_date, score)
VALUES
(1, 1, 'pass', '2024-02-05', 85),
(2, 2, 'fail', '2024-02-06', 40);

-- Insert data into Badge table
INSERT INTO Badge (badge_name, badge_description)
VALUES
('Top Scorer', 'Awarded to students scoring above 90'),
('Consistent Performer', 'Awarded for consistent performance across assessments');

-- Insert data into Student_badge table
INSERT INTO Student_badge (student_id, badge_id, date_awarded)
VALUES
(1, 1, '2024-02-10'),
(1, 2, '2024-02-15');

-- Insert data into Course_rating table
INSERT INTO Course_rating (rated_by, course_id, rating, comment)
VALUES
(1, 1, 5, 'Excellent course with great material'),
(2, 2, 4, 'Well-structured, but more examples would help');

-- Insert data into Notification table
INSERT INTO Notification (message, created_at)
VALUES
('New course content available for Math 101', '2024-01-28 10:00:00'),
('Assessment deadline approaching for Physics 202', '2024-01-29 15:00:00');

-- Insert data into Student_notification table
INSERT INTO Student_notification (student_id, notification_id, is_pushed)
VALUES
(1, 1, TRUE),
(2, 2, FALSE);
