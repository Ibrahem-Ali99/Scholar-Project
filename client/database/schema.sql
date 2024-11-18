-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS scholar;

-- Switch to the scholar database
USE scholar;

-- Table 1: Student
CREATE TABLE Student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Table 2: Teacher
CREATE TABLE Teacher (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Table 3: Course
CREATE TABLE Course (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- Table 4: Parent
CREATE TABLE Parent (
    parent_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- Table 5: Admin
CREATE TABLE Admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Table 6: Enrollment
CREATE TABLE Enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    student_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- Table 7: Payment
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Table 8: Course_content
CREATE TABLE Course_content (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    content_type VARCHAR(50) NOT NULL,
    post_date DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Table 9: Course_assessment
CREATE TABLE Course_assessment (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    max_score INT NOT NULL,
    post_date DATE NOT NULL,
    deadline DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Table 10: Student_progress
CREATE TABLE Student_progress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    assessment_id INT NOT NULL,
    status ENUM('pass', 'fail') NOT NULL,
    completion_date DATE,
    score INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (assessment_id) REFERENCES Course_assessment(assessment_id)
);

-- Table 11: Badge
CREATE TABLE Badge (
    badge_id INT AUTO_INCREMENT PRIMARY KEY,
    badge_name VARCHAR(100) NOT NULL,
    badge_description TEXT
);

-- Table 12: Student_badge
CREATE TABLE Student_badge (
    student_badge_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    badge_id INT NOT NULL,
    date_awarded DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (badge_id) REFERENCES Badge(badge_id)
);

-- Table 13: Course_rating
CREATE TABLE Course_rating (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    rated_by INT NOT NULL,
    course_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    FOREIGN KEY (rated_by) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Table 14: Notification
CREATE TABLE Notification (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    created_at DATETIME NOT NULL
);

-- Table 15: Student_notification
CREATE TABLE Student_notification (
    student_notification_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    notification_id INT NOT NULL,
    is_pushed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (notification_id) REFERENCES Notification(notification_id)
);
