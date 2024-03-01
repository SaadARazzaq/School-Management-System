# School Management System 🏫

## Description:
This OOP based School Management System is a Python program that allows users to perform CRUD (Create, Read, Update, Delete) operations on a database containing information about students, teachers, courses, and enrollments. It utilizes SQLite for database management and provides classes for each entity (Student, Teacher, Course, Enrollment) with methods for managing their respective data in the database.

## Student Class 🎓:
The `Student` class represents a student entity and contains methods for adding, updating, deleting, and printing student details.

### CRUD Operations 📝:
- **Add New Student:** Adds a new student to the database.
- **Update Student:** Updates an existing student's information in the database.
- **Delete Student:** Deletes an existing student from the database.
- **Print All Students Details:** Prints details of all students stored in the database.

## Teacher Class 👩‍🏫:
The `Teacher` class represents a teacher entity and provides methods for CRUD operations related to teachers.

### CRUD Operations 📝:
- **Add New Teacher:** Adds a new teacher to the database.
- **Update Teacher:** Updates an existing teacher's information in the database.
- **Delete Teacher:** Deletes an existing teacher from the database.
- **Print All Teachers Details:** Prints details of all teachers stored in the database.

## Course Class 📚:
The `Course` class represents a course entity and includes methods for CRUD operations related to courses.

### CRUD Operations 📝:
- **Add New Course:** Adds a new course to the database.
- **Update Course:** Updates an existing course's information in the database.
- **Delete Course:** Deletes an existing course from the database.
- **Print All Courses Details:** Prints details of all courses stored in the database.

## Enrollment Class 📝:
The `Enrollment` class handles operations related to student enrollments in courses and provides CRUD methods for managing enrollments.

### CRUD Operations 📝:
- **Add New Enrollment:** Adds a new enrollment record to the database.
- **Update Enrollment:** Updates an existing enrollment record in the database.
- **Delete Enrollment:** Deletes an existing enrollment record from the database.
- **Print All Enrollments Details:** Prints details of all enrollments stored in the database.

## Database Management 🗃️:
The program uses SQLite for database management. Tables for students, teachers, courses, and enrollments are created upon initialization.

## Usage 🚀:
1. Run the Python script.
2. Choose the desired option from the main menu to manage students, teachers, courses, or enrollments.
3. Follow the prompts to perform CRUD operations.

## Technologies Used 🛠️:
- Python
- SQLite

## Note 📌:
Ensure that the SQLite library is installed and accessible in your Python environment. The program creates and manages a SQLite database named `school.db` to store the school's information.
