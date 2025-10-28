HEAD
def addNumbers(num1, num2):
    return num1 + num2

def getValidnumber(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nInput interrupted. Exiting.")
            exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit(1)

def main():
    try:
        print("Welcome to the Simple Adder Program!")
        first_number = getValidnumber("Enter the first number: ")
        second_number = getValidnumber("Enter the second number: ")
        result = addNumbers(first_number, second_number)
        print(f"The sum is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
#hi po
main()


def addNumber(firstNumber, secondNumber):
    return firstNumber + secondNumber

def main():
    print("======This is a Simple Adder Program======") 

    while True:
      try:
          firstNumber = int(input("Enter the first number: "))
          secondNumber = int(input("Enter the second number: "))
          break

      except ValueError:
          print("INVALID INPUT!!! Please enter proper numeric values...")

    #RESULT
    result = addNumber(firstNumber, secondNumber)
    print("ANSWER: ", result)

main()
b518417 (Cleaned up messy code and added error handling)
