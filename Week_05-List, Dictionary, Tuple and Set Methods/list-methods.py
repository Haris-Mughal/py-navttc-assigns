fruits = ["apple", "banana", "cherry"]
print(f"Original List: {fruits}")

# Adding items
fruits.append("mango")
print(f"After append('mango'): {fruits}")

fruits.insert(1, "orange")
print(f"After insert(1, 'orange'): {fruits}")

# Removing items
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# Organizing
fruits.sort()
print(f"After sort() (Alphabetical): {fruits}")

fruits.reverse()
print(f"After reverse(): {fruits}")

# Information & Access
print(f"Final List Length: {len(fruits)}")
print(f"First element (Index 0): {fruits[0]}")