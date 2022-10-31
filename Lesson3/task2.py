from math import sqrt

def askNumbers():
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    return firstNumber, secondNumber

def plusNumbers(first, second):
    return first + second

def minusNumbers(first, second):
    return first - second

def divideNumbers(first, second):
    return first / second

def multiplyNumbers(first, second):
    return first * second

def powerNumbers(first, second):
    return first**2, second**2

def sqrtNumbers(first, second):
    return round(sqrt(first), 2), round(sqrt(second), 2)

def chooseFunction(first, second, choice):
    if choice == 1: return plusNumbers(first, second)
    elif choice == 2: return minusNumbers(first, second)
    elif choice == 3: return divideNumbers(first, second)
    elif choice == 4: return multiplyNumbers(first, second)
    elif choice == 5: return powerNumbers(first, second)
    elif choice == 6: return sqrtNumbers(first, second)
    else: return None

def main():
    userChoice = 1
    while userChoice != 0:
        firstNumber, secondNumber = askNumbers()
        print("\n1.Plus two numbers\n2.Minus two numbers\n3.Divide two numbers\n4.Multiply two numbers\n5.Find a power of two numbers\n6.Find a root of two numbers\n0.Exit\n")
        userChoice = int(input("Choose an operation to do: "))
        print("Result:", chooseFunction(firstNumber, secondNumber, userChoice))

main()