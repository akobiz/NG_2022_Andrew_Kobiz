
userNumber = int(input("Enter your number: "))
numberFactorial = 1
print(userNumber, end='')

while userNumber != 0:
    numberFactorial *= userNumber
    userNumber -= 1

print("! =", numberFactorial)