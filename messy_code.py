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

    #Operation & Result
    result = addNumber(firstNumber, secondNumber)
    print("ANSWER: ", result)

main()

