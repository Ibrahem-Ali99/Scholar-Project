-- Step 1: Drop the existing 'scholar' database if it exists
DROP DATABASE IF EXISTS scholar;

-- Step 2: Create a new 'scholar' database and select it for use
CREATE DATABASE scholar;
USE scholar;

-- Step 3: Create the Student table
CREATE TABLE Student (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Step 4: Create the Teacher table
CREATE TABLE Teacher (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Step 5: Create the Parent table
CREATE TABLE Parent (
    parent_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- Step 6: Create the Admin table
CREATE TABLE Admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Step 7: Create the Course table
CREATE TABLE Course (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT,
    teacher_id INT,
    price DECIMAL(10, 2) NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
);

-- Step 8: Create the CourseContent table
CREATE TABLE CourseContent (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    content_type VARCHAR(50) NOT NULL,
    post_date DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Step 9: Create the CourseAssessment table
CREATE TABLE CourseAssessment (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    max_score INT NOT NULL,
    post_date DATE NOT NULL,
    deadline DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Step 10: Create the CourseRating table
CREATE TABLE CourseRating (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    rated_by INT NOT NULL,
    course_id INT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    FOREIGN KEY (rated_by) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Step 11: Create the Enrollment table
CREATE TABLE Enrollment (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT NOT NULL,
    student_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);

-- Step 12: Create the Payment table
CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Step 13: Create the Badge table
CREATE TABLE Badge (
    badge_id INT AUTO_INCREMENT PRIMARY KEY,
    badge_name VARCHAR(100) NOT NULL,
    badge_description TEXT
);

-- Step 14: Create the StudentBadge table
CREATE TABLE StudentBadge (
    student_badge_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    badge_id INT NOT NULL,
    date_awarded DATE NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (badge_id) REFERENCES Badge(badge_id)
);

-- Step 15: Create the Notification table
CREATE TABLE Notification (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    message TEXT NOT NULL,
    created_at DATETIME NOT NULL
);

-- Step 16: Create the StudentNotification table
CREATE TABLE StudentNotification (
    student_notification_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    notification_id INT NOT NULL,
    is_pushed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (notification_id) REFERENCES Notification(notification_id)
);

-- Step 17: Create the StudentProgress table
CREATE TABLE StudentProgress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    assessment_id INT NOT NULL,
    status ENUM('pass', 'fail') NOT NULL,
    completion_date DATE,
    score INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (assessment_id) REFERENCES CourseAssessment(assessment_id)
);
