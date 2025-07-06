# Simple Calculator in Python
# By: Amna Noor

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

print("Welcome to Simple Calculator!")
print("Operations: +  -  *  /")

num1 = float(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print("Result:", add(num1, num2))
elif op == '-':
    print("Result:", subtract(num1, num2))
elif op == '*':
    print("Result:", multiply(num1, num2))
elif op == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operator!")

        
