# Student Management System using Nested Data Structures

students = []

# Add Student
def add_student():
    _id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")

    subjects = {}
    num_subjects = int(input("How many subjects? "))

    for _ in range(num_subjects):
        sub = input("Enter subject name: ")
        marks = list(map(int, input(f"Enter marks for {sub} (comma separated): ").split(",")))
        subjects[sub] = marks

    student = {
        "_id": _id,
        "name": name,
        "subjects": subjects
    }

    students.append(student)
    print("Student added successfully!\n")

# Display Students
def display_students():
    for s in students:
        print(f"\nID: {s['_id']} | Name: {s['name']}")
        for sub, marks in s["subjects"].items():
            print(f"  {sub}: {marks}")

# Calculate Average Marks
def calculate_average(student):
    total = 0
    count = 0

    for marks in student["subjects"].values():
        total += sum(marks)
        count += len(marks)

    return total / count if count != 0 else 0

# Show Result
def show_results():
    for s in students:
        avg = calculate_average(s)
        print(f"{s['name']} - Average: {avg:.2f}")

# Search Student
def search_student():
    search_id = int(input("Enter ID to search: "))
    for s in students:
        if s["_id"] == search_id:
            print(f"Found: {s['name']}")
            return
    print("Student not found!")

# Main Menu
while True:
    print("\n--- Student System ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Show Results")
    print("4. Search Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        show_results()
    elif choice == "4":
        search_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
