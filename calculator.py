# A Python Program for a Simple CLI Calculator for four basic Arithmeic Operations

# This function adds two numbers
def add(x, y):
    return x + y    # This Defines two variables and Adds them

# This function subtracts two numbers
def subtract(x, y):
    return x - y    # This Defines two variables and performs Substraction

# This function multiplies two numbers
def multiply(x, y):
    return x * y    # This Defines two variables and Multiplies this

# This function divides two numbers
def divide(x, y):
    return x / y    # This Defines two variables and performs Division


# Printing All the Available Options in the CLI Terminal
print()
print()
print("Select operation.")
print()
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print()
print()


# Printing The Corresponding Input Values for the Above Options Respectively
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    

    # Performing Relational & Logical Operations upon the Option given
    # check if choice is one of the four options

    if choice in ('1', '2', '3', '4'):      

        print()
        num1 = float(input("Enter first number: ")) # First Operand Number

        print()
        num2 = float(input("Enter second number: "))    # Second Operand Number


        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))    # Addition Operation

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))   # Substraction Operation

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))   # Multiplication Operation

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2)) # Division Operation


        # check if user wants another calculation
        # break the while loop if answer is no 
        print()
        print()
        
        next_calculation = input("Let's do next calculation? (yes/no): ")   # Whether Next Calculation Or Not

        if next_calculation == "no":    # Yes for 'Loop'/No for 'Break Loop'
          break    
        
    else:
        print()
        print("Invalid Input")  # Printing Error For Incorrect Input