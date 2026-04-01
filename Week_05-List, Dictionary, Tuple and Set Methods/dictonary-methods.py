student = {"name": "Ali", "age": 20, "grade": "A"}
print(f"Original Dictionary: {student}")

# Accessing Data
print(f"Retrieved Name: {student.get('name')}")

# Modifying Data
student["city"] = "Lahore"
print(f"After adding 'city': {student}")

student.update({"grade": "A+"})
print(f"After update('grade'): {student}")

# Deleting Data
student.pop("age")
print(f"After pop('age'): {student}")

# View Objects
print(f"Dictionary Keys: {list(student.keys())}")
print(f"Dictionary Values: {list(student.values())}")

# Resetting
student.clear()
print(f"After clear(): {student}")