import json

students = []


# Save student data into JSON file
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


# Load student data from JSON file
def load_data():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []


def get_marks(subject):
    while True:

        try:
            marks = int(input(f"Enter {subject} Marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            else:
                print("Marks must be between 0 and 100!")

        except ValueError:
            print("Please enter a valid number!")

# Add Student
def add_student():
    print("\n===== ADD STUDENT =====")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    python_marks = get_marks("Python")
    FSD_marks = get_marks("FSD")
    DE_marks = get_marks("DE")

    total = python_marks + FSD_marks + DE_marks
    percentage = total / 3

    # Calculate Grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Calculate Result
    if percentage >= 35:
        status = "PASS"
    else:
        status = "FAIL"

    student = {
        "id": student_id,
        "name": name,
        "python": python_marks,
        "FSD": FSD_marks,
        "DE": DE_marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }

    students.append(student)

    # Save data
    save_data()

    print("\nStudent added successfully!")
    print("Total:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Status:", status)


# View All Students
def view_students():
    print("\n===== ALL STUDENTS =====")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("----------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Percentage:", round(student["percentage"], 2), "%")
        print("Grade:", student["grade"])
        print("Status:", student["status"])


# Search Student
def search_student():
    print("\n===== SEARCH STUDENT =====")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            print("----------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Python:", student["python"])
            print("FSD:", student["FSD"])
            print("DE:", student["DE"])
            print("Total:", student["total"], "/ 300")
            print("Percentage:", round(student["percentage"], 2), "%")
            print("Grade:", student["grade"])
            print("Status:", student["status"])

            return

    print("Student not found.")


# Delete Student
def delete_student():
    print("\n===== DELETE STUDENT =====")

    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            # Save updated data
            save_data()

            print("Student deleted successfully!")

            return

    print("Student not found.")


# Load existing data when program starts
load_data()


# Main Menu
while True:

    print("\n===================================")
    print(" STUDENT RESULT MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using the system!")
        break

    else:
        print("\nInvalid choice! Please try again.")