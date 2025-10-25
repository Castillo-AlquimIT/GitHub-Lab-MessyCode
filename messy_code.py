def addNumbers(num1, num2):
    return num1 + num2

def getValidnumber(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the Simple Adder Program!")
    
    first_number = getValidnumber("Enter the first number: ")
    second_number = getValidnumber("Enter the second number: ")
    
    result = addNumbers(first_number, second_number)
    print(f"The sum is: {result}")

main()