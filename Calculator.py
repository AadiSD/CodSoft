# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator loop
while True:
    # Display menu
    print("Select Arithmetic Operation : ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5) : ")

    if choice == '5':
        print("Calculator has been closed.")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid input. Please try again.")
        continue

    # Input two numbers
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    if choice == '1':
        result = add(num1, num2)
        operation = "addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "division"

    print(f"The result of {operation} is: {result}")
