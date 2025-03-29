## Task 1
## Write a simple Python program that checks whether each number from 1 to 15 is even or odd


for i in range(1, 15):
    if i%2==0:
        print("The number", i, "is even")
    else:
        print("The number", i, "is odd")

##Task 2
## Create a program that acts as a simple calculator. The program should ask the user to enter two numbers and then choose an operation (addition, subtraction, multiplication, or division).

print("This is a Simple Calculator for Basic Arithmetic Operation (+, -, *, /)")

try:
    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    print("\nChoose an operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("/ for division")
    print("* for multiplication")

    operation = str(input("Choose an operation (+, -, *, /): "))

    if operation == "+":
            print(f"\n{num1} + {num2} = {num1+num2}")
    elif operation == "-":
            print(f"\n{num1} - {num2} = {num1-num2}")
    elif operation == "*":
          print(f"\n{num1} * {num2} = {num1*num2}")
    elif operation == "/":
            print(f"\n{num1} / {num2} = {num1/num2}")



except ValueError:
    print("Error: Please enter a valid number!")
except Exception as e:
      print(f"An unexpected error occured: {e}")
