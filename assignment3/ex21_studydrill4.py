# 24 + 34 / 100 - 1023

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDNG {a} / {b}")
    return a / b

answer = subtract(add(24, divide(24, 100)), 1023)

print(answer)
