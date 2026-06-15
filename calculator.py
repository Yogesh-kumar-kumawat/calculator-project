def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def floor_division(a, b):
    return a // b


print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Power:", power(10, 2))
print("Modulus:", modulus(10, 3))
print("Floor Division:", floor_division(10, 3))