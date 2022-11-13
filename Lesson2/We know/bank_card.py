def checkStartNumbersCard(startNumbers, userCard):
    for numbers in range(len(startNumbers)):
        if int(userCard[:2]) == startNumbers[numbers]:
            return True

def checkCardType(userCard):
    if (len(userCard) == 13 or len(userCard) == 16) and int(userCard[0]) == bankCards["VISA"]:
        print("VISA", end=' ')
    elif len(userCard) == 16:
        if checkStartNumbersCard(bankCards["MASTERCARD"], userCard): 
            print("MASTERCARD", end=' ')
    elif len(userCard) == 15:
        if checkStartNumbersCard(bankCards["AMEX"], userCard):
            print("AMEX", end=' ')
    else:
        print("INVALID")

def calculateSumByTwo(userCard):
    sumByTwo = []
    while len(userCard):
        sumByTwo.append(int(userCard[-1]) * 2)
        if sumByTwo[-1] > 9:
            sumByTwo.append((sumByTwo[-1] % 10))
            sumByTwo[-2] = int(sumByTwo[-2] / 10)
        userCard = userCard[:-2]
    return sumByTwo

def calculateRestSum(userCard):
    restSum = []
    while len(userCard):
        restSum.append(int(userCard[-1]))
        userCard = userCard[:-2]
    return restSum

def checkCardIsLegit(userCard):
    sumOfCard = sum(calculateSumByTwo(list(userCard[:-1]))) + sum(calculateRestSum(list(userCard)))
    if sumOfCard % 10 == 0:
        checkCardType(userCard)
    else:
        print("INVALID")

bankCards = {
    "VISA": 4,
    "MASTERCARD": [51, 52, 53, 54, 55],
    "AMEX": [34, 37],
} # start numbers in each banks

userCard = input("Enter your bank card: ")
checkCardIsLegit(userCard)
