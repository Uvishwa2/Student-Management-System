students = []


def add_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    course = input("Enter course: ").strip()

    if not name or not roll_no or not course:
        print("All fields are required.")
        return
    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course
    }

    students.append(student)
    print("Student added successfully.")


def view_students():
    if not students:
        print("No student records found.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Course:", student["course"])
        print("--------------------")

def update_student():
    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new student name: ")
            student["course"] = input("Enter new course: ")

            print("Student updated successfully.")
            return

    print("Student not found.")        

def delete_student():
    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")

def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("Student found.")
            print("Name:", student["name"])
            print("Roll No:", student["roll_no"])
            print("Course:", student["course"])
            return

    print("Student not found.")


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
            
            print("Thank you.")
            break
        else:
            print("Invalid choice.")


main()
