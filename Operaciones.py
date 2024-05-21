def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero not allowed."
    return a / b

# Request two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition_result = addition(num1, num2)
subtraction_result = subtraction(num1, num2)
multiplication_result = multiplication(num1, num2)
division_result = division(num1, num2)

# Print results in Spanish
print(f"Suma: {addition_result}")
print(f"Resta: {subtraction_result}")
print(f"Multiplicación: {multiplication_result}")
print(f"División: {division_result}")
