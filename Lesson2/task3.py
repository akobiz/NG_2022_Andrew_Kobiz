userSize = int(input("Enter your size: "))
tmpSize = userSize

while userSize != 0:
    if tmpSize != 0:
        print(tmpSize, end=' ')
        tmpSize -= 1
    elif tmpSize == 0:
        userSize -= 1
        tmpSize = userSize
        print()