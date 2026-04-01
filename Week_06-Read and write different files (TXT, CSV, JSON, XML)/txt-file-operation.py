import os

# --- Step 1: Create and Write to a File ---
# 'w' mode: creates a new file or overwrites existing content
file = open("student_data.txt", "w")
file.write("Name: Haris\n")
file.write("Class: 16\n")
file.write("Marks: 85\n")
file.close()
print("File created and data written successfully!\n")

# --- Step 2: Read Data from the File ---
file = open("student_data.txt", "r")
content = file.read()
print("Current Content:")
print("-" * 15)
print(content)
file.close()

# --- Step 3: Append More Data to the File ---
# 'a' mode: adds data to the end of the file
file = open("student_data.txt", "a")
file.write("Grade: A\n")
file.close()
print("New data 'Grade: A' appended successfully!\n")

# --- Step 4: Secure Reading (Using 'with' statement) ---
# The 'with' statement automatically closes the file for us
with open("student_data.txt", "r") as file:
    print(file.read())

# --- Step 5: Delete File ---
if os.path.exists("student_data.txt"):
    os.remove("student_data.txt")
    print("File 'student_data.txt' deleted successfully.")
else:
    print("Error: File not found.")