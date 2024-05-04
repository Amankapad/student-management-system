import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="student_info"
)
cursor = mydb.cursor()

class StudentInformationSystem:
    def __init__(self):
        pass

    def add_student(self, student_id, name, branch, course, semester, age):
        try:
            sql = "INSERT INTO students (student_id, name, branch, course, semester, age) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (student_id, name, branch, course, semester, age)
            cursor.execute(sql, val)
            mydb.commit()
            print("Student added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def view_students(self):
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        if result:
            print("Student Records:")
            print("ID\tName\tBranch\tCourse\tSemester\tAge")
            for row in result:
                print("\t".join(str(item) for item in row))
        else:
            print("No students found.")

    def search_student_by_id(self, student_id):
        try:
            sql = "SELECT * FROM students WHERE student_id = %s"
            val = (student_id,)
            cursor.execute(sql, val)
            result = cursor.fetchall()
            if result:
                print("Student Found:")
                print("ID\tName\tBranch\tCourse\tSemester\tAge")
                for row in result:
                    print("\t".join(str(item) for item in row))
            else:
                print("Student not found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def search_student_by_name(self, name):
        try:
            sql = "SELECT * FROM students WHERE name = %s"
            val = (name,)
            cursor.execute(sql, val)
            result = cursor.fetchall()
            if result:
                print("Students Found:")
                print("ID\tName\tBranch\tCourse\tSemester\tAge")
                for row in result:
                    print("\t".join(str(item) for item in row))
            else:
                print("Student not found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def update_student(self, student_id, branch, course, semester, age):
        try:
            sql = "UPDATE students SET branch = %s, course = %s, semester = %s, age = %s WHERE student_id = %s"
            val = (branch, course, semester, age, student_id)
            cursor.execute(sql, val)
            mydb.commit()
            print("Student information updated successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def delete_student(self, student_id):
        try:
            sql = "DELETE FROM students WHERE student_id = %s"
            val = (student_id,)
            cursor.execute(sql, val)
            mydb.commit()
            print("Student deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

def main():
    sis = StudentInformationSystem()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by ID")
        print("4. Search Student by Name")
        print("5. Update Student Information")
        print("6. Delete Student")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            course = input("Enter Course: ")
            semester = int(input("Enter Semester: "))
            age = int(input("Enter Age: "))
            sis.add_student(student_id, name, branch, course, semester, age)
        elif choice == "2":
            sis.view_students()
        elif choice == "3":
            student_id = int(input("Enter Student ID to search: "))
            sis.search_student_by_id(student_id)
        elif choice == "4":
            name = input("Enter Name to search: ")
            sis.search_student_by_name(name)
        elif choice == "5":
            student_id = int(input("Enter Student ID to update: "))
            branch = input("Enter Branch: ")
            course = input("Enter Course: ")
            semester = int(input("Enter Semester: "))
            age = int(input("Enter Age: "))
            sis.update_student(student_id, branch, course, semester, age)
        elif choice == "6":
            student_id = int(input("Enter Student ID to delete: "))
            sis.delete_student(student_id)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
