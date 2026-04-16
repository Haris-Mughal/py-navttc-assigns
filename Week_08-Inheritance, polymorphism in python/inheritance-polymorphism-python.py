# --- Base Class ---
class Person:
    """Base class for all people in the school"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

    def __str__(self):
        return self.get_details()


# --- Inheritance: Derived Class 1 ---
class Student(Person):
    """Student inherits from Person"""
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks  # dictionary: subject → marks

    # --- Polymorphism: override method ---
    def get_details(self):
        avg = sum(self.marks.values()) / len(self.marks)
        return f" Student: {self.name} (Roll No: {self.roll_no}, Age: {self.age}, Avg Marks: {avg:.2f})"

    # --- Operator Overloading ---
    def __add__(self, other):
        """Add total marks of two students"""
        if isinstance(other, Student):
            total1 = sum(self.marks.values())
            total2 = sum(other.marks.values())
            return total1 + total2
        raise TypeError("Addition allowed only between Student objects")

    def __gt__(self, other):
        """Compare students by average marks"""
        if isinstance(other, Student):
            avg1 = sum(self.marks.values()) / len(self.marks)
            avg2 = sum(other.marks.values()) / len(other.marks)
            return avg1 > avg2
        raise TypeError("Comparison allowed only between Student objects")


# --- Inheritance: Derived Class 2 ---
class Teacher(Person):
    """Teacher inherits from Person"""
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    # --- Polymorphism: override method ---
    def get_details(self):
        return f" Teacher: {self.name} teaches {self.subject}, Salary: Rs.{self.salary}"


# --- Composition: School has Students and Teachers ---
class School:
    """School class composed of Student and Teacher objects"""
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f" Added Student: {student.name}")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"✅ Added Teacher: {teacher.name}")

    def show_all(self):
        print(f"\n School: {self.name}")
        print("\n-- Teachers --")
        for t in self.teachers:
            print(t.get_details())
        print("\n-- Students --")
        for s in self.students:
            print(s.get_details())
        print("----------------------------")

    def total_students(self):
        return len(self.students)

    def total_teachers(self):
        return len(self.teachers)


# --- Main Program ---
def main():
    print("Welcome to School Management System\n")

    # Create school (Composition)
    school = School("City Public School")

    # Create teachers
    t1 = Teacher("Ali Raza", 40, "Math", 75000)
    t2 = Teacher("Aiman Khan", 35, "English", 70000)

    # Create students
    s1 = Student("Hassan", 15, 101, {"Math": 85, "English": 78, "Science": 90})
    s2 = Student("Ayesha", 16, 102, {"Math": 92, "English": 88, "Science": 95})
    s3 = Student("Bilal", 15, 103, {"Math": 70, "English": 65, "Science": 75})

    # Add to school
    school.add_teacher(t1)
    school.add_teacher(t2)
    school.add_student(s1)
    school.add_student(s2)
    school.add_student(s3)

    # Show details
    school.show_all()

    # Operator Overloading examples
    print("\n --- Operator Overloading ---")
    total_marks = s1 + s2
    print(f"Combined total marks of {s1.name} and {s2.name}: {total_marks}")

    print("\n --- Comparing Students ---")
    print(f"Is {s2.name} better than {s1.name}? {'Yes' if s2 > s1 else 'No'}")

    print("\n --- School Summary ---")
    print(f"Total Students: {school.total_students()}")
    print(f"Total Teachers: {school.total_teachers()}")


# Run program
if __name__ == "__main__":
    main()
