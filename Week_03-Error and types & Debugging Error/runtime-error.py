a = 10
b = 0
result = a / b    # Error: Program crashes here
print("Result is:", result)

# Corrected code:
if b != 0:
    result = a / b
    print("Result is:", result)
else:
    print("Error: Cannot divide by zero.")