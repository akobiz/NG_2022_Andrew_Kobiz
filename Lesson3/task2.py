
def showInfo():
    print("\n===============================================")
    print("1.Sort string.\n2.Calculate count of all elements in string\n" \
        "3.Show vowal chars in string.\n4.Show consonants chars in string\n" \
            "5.Split and show reversed string.\n6.Show word by index.\n" \
                "7.Enter string again.\n0.Exit")
    print("===============================================\n")

def askString():
    stringUser = input("Enter your string: ")
    return stringUser

def elemCount(string):
    return len(string)

def sortString(string):
    return sorted(string)

def showVowalsAndConsonants(string, choice):
    vowels = "AEIOUY"
    if choice == 0:
        for char in range(0, len(string)):
            for vowel in range(0, len(vowels)):
                if string[char].upper() == vowels[vowel].upper():
                    print(string[char], end=' ')
    elif choice == 1:
        for char in range(len(string)):
            for vowel in range(len(vowels)):
                if string[char].upper() == vowels[vowel].upper():
                    break
                elif string[char].upper() != vowels[vowel].upper() and vowel + 1 == len(vowels):
                    print(string[char], end='')

def splitAndReverseString(string):
    string = string.split(" ")
    for word in reversed(string):
        print(word, end=' ')
        
def findWordInString(string, index):
    return string[index-1]

def chooseFunction(string, choice):
    if choice == 1:
        print("Sorted string by char: ", sortString(string.replace(" ", "")))
    elif choice == 2:
        print("Elements in string: ", elemCount(string))
    elif choice == 3:
        showVowalsAndConsonants(string, 0)
    elif choice == 4:
        showVowalsAndConsonants(string, 1)
    elif choice == 5:
        splitAndReverseString(string)
    elif choice == 6:
        index = int(input("Enter index: "))
        print(findWordInString(string.split(" "), index))

def main():
    userChoice = 1
    stringUser = askString()
    while userChoice != 0:
        showInfo()
        userChoice = int(input("Choose an operation to do: "))
        if userChoice == 7:
            stringUser = askString()
        chooseFunction(stringUser, userChoice)
        
main()