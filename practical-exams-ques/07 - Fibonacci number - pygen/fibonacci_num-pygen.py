import itertools

def fibonacci_gen():
    """A generator that yields Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

first_15 = itertools.islice(fibonacci_gen(), 15)

print("First 15 Fibonacci Numbers:")
print(list(first_15))

