from math import sqrt

firstNumber = int(input("Enter a first number: "))
secondNumber = int(input("Enter a second number: "))
operationChoose = int(input("Choose an operation:\n1.Add two numbers.\n2.Minus two numbers.\n3.Multiply two numbers.\n4.Division two numbers.\n5.Find the square and root of two numbers"))

if operationChoose == 1:
    print("Result: ", firstNumber + secondNumber)
elif operationChoose == 2:
    print("Result: ", firstNumber - secondNumber)
elif operationChoose == 3:
    print("Result: ", firstNumber * secondNumber)
elif operationChoose == 4:
    print("Result: ", firstNumber / secondNumber)
elif operationChoose == 5:
    print("Result:\nFirst number in pow(2):", pow(firstNumber, 2),"and second number in pow(2):", pow(secondNumber, 2))
    print("Root of first number:", round(sqrt(firstNumber), 2),"and root of second number:", round(sqrt(secondNumber), 2))
