import sqlite3

#  Student class that contains crud operations for the student
class Student:
    def __init__(self, StudentID, StudentName):
        self.StudentID = StudentID
        self.StudentName = StudentName
    
    def print_student_details(self):
        print('Student Id:', self.StudentID, ', Student Name:', self.StudentName)

    @staticmethod
    def print_all_students_details(cursor, connection):  # Print all the students
        try:
            cursor.execute("SELECT * FROM StudentsCoursesRegistraions")
            students = cursor.fetchall()
            for student in students:
                print(student)
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def add_new_student(self, cursor, connection):  # Add a new student to db
        while True:
            try:
                self.StudentID = int(input('Input student id: '))
                cursor.execute("INSERT INTO StudentsCoursesRegistraions (StudentID, StudentName) VALUES (?, ?)", (self.StudentID, self.StudentName))
                connection.commit()
                print('Student Added Successfully')
                break  # Break out of the loop if insertion is successful
            except ValueError:
                print("Invalid input. Student ID must be an integer.")
            except sqlite3.Error as e:
                print("An error occurred:", e)

    def update_student(self, cursor, connection):  #  Update existing students in db
        try:
            cursor.execute("UPDATE StudentsCoursesRegistraions SET StudentName = ? WHERE StudentID = ?", (self.StudentName, self.StudentID))
            connection.commit()
            print('Student Updated Successfully')
        except sqlite3.Error as e:
            print("An error occurred:", e)

    @staticmethod
    def delete_student(StudentID, cursor, connection):  #  Delete an existing student from the db
        try:
            cursor.execute("DELETE FROM StudentsCoursesRegistraions WHERE StudentID = ?", (StudentID,))
            connection.commit()
            print('Student Deleted Successfully')
        except sqlite3.Error as e:
            print("An error occurred:", e)

#  Teacher class that contains crud operations for the Teachers
class Teacher:
    def __init__(self, TeacherID, TeacherName):
        self.TeacherID = TeacherID
        self.TeacherName = TeacherName
    
    def print_teacher_details(self):  
        print('Teacher Id:', self.TeacherID, ', Teacher Name:', self.TeacherName)

    @staticmethod
    def print_all_teachers(cursor, connection):  # Print all the teachers 
        try:
            cursor.execute("SELECT * FROM Teachers")
            teachers = cursor.fetchall()
            for teacher in teachers:
                print(teacher)
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def add_new_teacher(self, cursor, connection):  # add new teacher 
        try:
            cursor.execute("INSERT INTO Teachers (TeacherID, TeacherName) VALUES (?, ?)", (self.TeacherID, self.TeacherName))
            connection.commit()
            print('Teacher Added Successfully')
        except sqlite3.Error as e:
            print("An error occurred:", e)

    def update_teacher(self, cursor, connection):  # update a existing teacher
        try:
            cursor.execute("UPDATE Teachers SET TeacherName = ? WHERE TeacherID = ?", (self.TeacherName, self.TeacherID))
            connection.commit()
            print('Teacher Updated Successfully')
        except sqlite3.Error as e:
            print("An error occurred:", e)

    @staticmethod
    def delete_teacher(TeacherID, cursor, connection):  # Delete exisitng teacher
        try:
            cursor.execute("DELETE FROM Teachers WHERE TeacherID = ?", (TeacherID,))
            connection.commit()
            print('Teacher Deleted Successfully')
        except sqlite3.Error as e:
            print("An error occurred:", e)

#  Crud operations for courses class
class Course:
    def __init__(self, CourseID, CourseName):
        self.CourseID = CourseID
        self.CourseName = CourseName
    
    def print_course_details(self):
        print('Course Id:', self.CourseID, ', Course Name:', self.CourseName)

    @staticmethod
    def print_all_courses(cursor, connection):  #  Print all courses from db
        try:
            cursor.execute("SELECT * FROM Courses")
            courses = cursor.fetchall()
            for course in courses:
                print(course)
        except sqlite3.Error as e:
            print("Error:", e)
            print("Failed to retrieve courses from database.")

    def add_new_course(self, cursor, connection):  #  Add a new course to the db
        try:
            cursor.execute("INSERT INTO Courses (CourseID, CourseName) VALUES (?, ?)", (self.CourseID, self.CourseName))
            connection.commit()
            print('Course Added Successfully')
        except sqlite3.IntegrityError as e:
            print("Error:", e)
            print("Failed to add course. CourseID already exists.")

    def update_course(self, cursor, connection):  #  Update an existing course from the db
        try:
            cursor.execute("UPDATE Courses SET CourseName = ? WHERE CourseID = ?", (self.CourseName, self.CourseID))
            connection.commit()
            print('Course Updated Successfully')
        except sqlite3.Error as e:
            print("Error:", e)
            print("Failed to update course.")

    @staticmethod
    def delete_course(CourseID, cursor, connection):  #  Delete an exisitng course from the db
        try:
            cursor.execute("DELETE FROM Courses WHERE CourseID = ?", (CourseID,))
            connection.commit()
            print('Course Deleted Successfully')
        except sqlite3.Error as e:
            print("Error:", e)
            print("Failed to delete course.")

# This class has all the crud operations for managing all the enrollments 
class Enrollment:
    def __init__(self, EnrollmentID, StudentID, CourseID):
        self.EnrollmentID = EnrollmentID
        self.StudentID = StudentID
        self.CourseID = CourseID

    def add_new_enrollment(self, cursor, connection):  # To add new enrllment
        try:
            cursor.execute("INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID) VALUES (?, ?, ?)",
                           (self.EnrollmentID, self.StudentID, self.CourseID))
            connection.commit()
            print('Enrollment Added Successfully')
        except sqlite3.IntegrityError as e:
            print("Error:", e)
            print("Failed to add enrollment. EnrollmentID already exists.")

    def update_enrollment(self, cursor, connection):  # To update an existing enrllment
        try:
            cursor.execute("UPDATE Enrollments SET StudentID = ?, CourseID = ? WHERE EnrollmentID = ?",
                           (self.StudentID, self.CourseID, self.EnrollmentID))
            connection.commit()
            print('Enrollment Updated Successfully')
        except sqlite3.Error as e:
            print("Error:", e)
            print("Failed to update enrollment.")

    def delete_enrollment(self, cursor, connection):  # To delete an existing enrllment
        try:
            cursor.execute("DELETE FROM Enrollments WHERE EnrollmentID = ?", (self.EnrollmentID,))
            connection.commit()
            print('Enrollment Deleted Successfully')
        except sqlite3.Error as e:
            print("Error:", e)
            print("Failed to delete enrollment.")

    @staticmethod
    def print_all_enrollments(cursor, connection):   #  To print all the enrollments from the db
        try:
            cursor.execute("SELECT * FROM Enrollments")
            enrollments = cursor.fetchall()
            for enrollment in enrollments:
                print(enrollment)
        except sqlite3.Error as e:
            print("Error:", e)
            print("Failed to retrieve enrollments from database.")

    def print_enrollment_details(self):
        print('Enrollment Id:', self.EnrollmentID, ', Student ID:', self.StudentID, ', Course ID:', self.CourseID)

# The below function creates all the tables required in the db
def create_tables(cursor, connection):
    cursor.execute('''CREATE TABLE IF NOT EXISTS StudentsCoursesRegistraions (
                        StudentID    INTEGER PRIMARY KEY,
                        StudentName  TEXT,
                        CourseID     INTEGER,
                        Course_Details TEXT,
                        TeacherID    INTEGER,
                        Teacher_name TEXT,
                        Registration_Date TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Teachers (
                        TeacherID INTEGER PRIMARY KEY,
                        TeacherName TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                        CourseID INTEGER PRIMARY KEY,
                        CourseName TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
                        EnrollmentID INTEGER PRIMARY KEY,
                        StudentID INTEGER,
                        CourseID INTEGER,
                        FOREIGN KEY (StudentID) REFERENCES StudentsCoursesRegistraions(StudentID),
                        FOREIGN KEY (CourseID) REFERENCES Courses(CourseID))''')

    connection.commit()

# Menu for managing students
def student_management_menu(cursor, connection):
    while True:
        print('\nYou have chosen Student Management:')
        print('1. Add a new student')
        print('2. Update an existing student')
        print('3. Delete a student')
        print('4. View all students details')
        print('5. Back to main menu')

        choice = input('Input your choice: ')

        if choice == '1':
            try:
                StudentID = input('Input student id: ')
                StudentName = input('Input student name: ')
                s = Student(StudentID, StudentName)
                s.add_new_student(cursor, connection)
                s.print_student_details()
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '2':
            try:
                StudentID = input('Which student detail you want to update: input student id: ')
                StudentName = input('Input an updated student name: ')
                s = Student(StudentID, StudentName)
                s.update_student(cursor, connection)
                s.print_student_details()
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '3':
            try:
                StudentID = input('Input student id to delete: ')
                Student.delete_student(StudentID, cursor, connection)
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '4':
            try:
                Student.print_all_students_details(cursor, connection)
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '5':
            break
        else:
            print('Invalid input. Please choose a valid option.')

# Menu for managing teachers
def teacher_management_menu(cursor, connection):
    while True:
        print('\nYou have chosen Teacher Management:')
        print('1. Add a new teacher')
        print('2. Update an existing teacher')
        print('3. Delete a teacher')
        print('4. View all teachers details')
        print('5. Back to main menu')

        choice = input('Input your choice: ')

        if choice == '1':
            try:
                TeacherID = input('Input teacher id: ')
                TeacherName = input('Input teacher name: ')
                t = Teacher(TeacherID, TeacherName)
                t.add_new_teacher(cursor, connection)
                t.print_teacher_details()
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '2':
            try:
                TeacherID = input('Which teacher detail you want to update: input teacher id: ')
                TeacherName = input('Input an updated teacher name: ')
                t = Teacher(TeacherID, TeacherName)
                t.update_teacher(cursor, connection)
                t.print_teacher_details()
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '3':
            try:
                TeacherID = input('Input teacher id to delete: ')
                Teacher.delete_teacher(TeacherID, cursor, connection)
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '4':
            try:
                Teacher.print_all_teachers(cursor, connection)
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '5':
            break
        else:
            print('Invalid input. Please choose a valid option.')

# Menu for managing courses
def course_management_menu(cursor, connection):
    while True:
        print('\nYou have chosen Course Management:')
        print('1. Add a new course')
        print('2. Update an existing course')
        print('3. Delete a course')
        print('4. View all courses details')
        print('5. Back to main menu')

        choice = input('Input your choice: ')

        if choice == '1':
            try:
                CourseID = input('Input course id: ')
                CourseName = input('Input course name: ')
                c = Course(CourseID, CourseName)
                c.add_new_course(cursor, connection)
                c.print_course_details()
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '2':
            try:
                CourseID = input('Which course detail you want to update: input course id: ')
                CourseName = input('Input an updated course name: ')
                c = Course(CourseID, CourseName)
                c.update_course(cursor, connection)
                c.print_course_details()
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '3':
            try:
                CourseID = input('Input course id to delete: ')
                Course.delete_course(CourseID, cursor, connection)
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '4':
            try:
                Course.print_all_courses(cursor, connection)
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '5':
            break
        else:
            print('Invalid input. Please choose a valid option.')

# Menu for managing enrollments
def enrollment_management_menu(cursor, connection):
    while True:
        print('\nYou have chosen Enrollment Management:')
        print('1. Add a new enrollment')
        print('2. Update an existing enrollment')
        print('3. Delete an enrollment')
        print('4. View all enrollments details')
        print('5. Back to main menu')

        choice = input('Input your choice: ')

        if choice == '1':
            try:
                EnrollmentID = input('Input enrollment id: ')
                StudentID = input('Input student id: ')
                CourseID = input('Input course id: ')
                e = Enrollment(EnrollmentID, StudentID, CourseID)
                e.add_new_enrollment(cursor, connection)
                e.print_enrollment_details()
            except Exception as e:
                print("Error:", e)
        elif choice == '2':
            try:
                EnrollmentID = input('Which enrollment detail you want to update: input enrollment id: ')
                StudentID = input('Input updated student id: ')
                CourseID = input('Input updated course id: ')
                e = Enrollment(EnrollmentID, StudentID, CourseID)
                e.update_enrollment(cursor, connection)
                e.print_enrollment_details()
            except Exception as e:
                print("Error:", e)
        elif choice == '3':
            try:
                EnrollmentID = input('Input enrollment id to delete: ')
                Enrollment.delete_enrollment(EnrollmentID, cursor, connection)
            except Exception as e:
                print("Error:", e)
        elif choice == '4':
            try:
                Enrollment.print_all_enrollments(cursor, connection)
            except Exception as e:
                print("Error:", e)
        elif choice == '5':
            break
        else:
            print('Invalid input. Please choose a valid option.')

def main_menu(cursor, connection):
    while True:
        print('\nWhat would you like to manage:')
        print('0. Quit')
        print('1. Students')
        print('2. Teachers')
        print('3. Courses')
        print('4. Enrollment')

        choice = input('Input your choice: ')

        try:
            if choice == '1':
                student_management_menu(cursor, connection)
            elif choice == '2':
                teacher_management_menu(cursor, connection)
            elif choice == '3':
                course_management_menu(cursor, connection)
            elif choice == '4':
                enrollment_management_menu(cursor, connection)
            elif choice == '0':
                break
            else:
                print('Invalid input. Please choose a valid option.')
        except Exception as e:
            print("An error occurred:", e)

# make connection with db
connection = sqlite3.connect('school.db')

cursor = connection.cursor()

# create tables
create_tables(cursor, connection)

main_menu(cursor, connection)

# Close the connection
connection.close()
