# Function to add two numbers
def add(x, y):
    return x + y

# Function to substract two numbers
def substract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x , y ):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero not allowed"
    else:
        return x / y
    
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user:
        choice = input("Enter choices: 1,2,3,4: ")

        # Check if the input is one of the four options:
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter your second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {substract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            
        # option to exit the loop:
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            break
    print("Exiting calculator, chao!")

# Call the calculator function:
calculator()