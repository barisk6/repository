import math

# Function to handle the operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def square_root(x):
    if x < 0:
        return "Error! Negative value for square root."
    else:
        return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Main program loop
def calculator():
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square Root (√)")
    print("6. Power (x^y)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    
    while True:
        choice = input("Enter the operation number (1/2/3/4/5/6/7/8/9) or 'exit' to quit: ")
        
        if choice == 'exit':
            print("Exiting the calculator...")
            break
        elif choice in ['1', '2', '3', '4', '6']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '6':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
        
        elif choice == '5':
            num = float(input("Enter the number: "))
            print(f"√{num} = {square_root(num)}")
        
        elif choice == '7':
            angle = float(input("Enter the angle in degrees: "))
            print(f"sin({angle}) = {sine(angle)}")
        
        elif choice == '8':
            angle = float(input("Enter the angle in degrees: "))
            print(f"cos({angle}) = {cosine(angle)}")
        
        elif choice == '9':
            angle = float(input("Enter the angle in degrees: "))
            print(f"tan({angle}) = {tangent(angle)}")
        
        else:
            print("Invalid input! Please choose a valid operation.")

# Run the calculator
calculator()
