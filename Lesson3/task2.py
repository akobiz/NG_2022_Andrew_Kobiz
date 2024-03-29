def showInfo(stringUser):
    print("\n===============================================")
    print("1.Sort string.\n2.Calculate count of all elements in string\n" \
        "3.Show vowal chars in string.\n4.Show consonants chars in string\n" \
            "5.Split and show reversed string.\n6.Show word by index.\n" \
                "7.Enter string again.\n0.Exit")
    print("===============================================\nYour string: " + stringUser)

def askString():
    return input("Enter your string: ")

def showVowalsAndConsonants(string, choice):
    vowels = "AaEeIiOoUuYy"
    result = []
    match choice:
        case 0:
            result = [each for each in string if each in vowels]
            print(result)
        case 1:
            result = [each for each in string if each not in vowels]
            print(result)


def splitAndReverseString(string):
    string.reverse()
    print(" ".join(string))
        
def findWordInString(string, index):
    return string[index-1]

def chooseFunction(string, choice):
    match choice:
        case 1:
            print("Sorted string by char: ", sorted(string.replace(" ", "")))
        case 2:
            print("Elements in string: ", len(string))
        case 3:
            showVowalsAndConsonants(string.replace(" ", ""), 0)
        case 4:
            showVowalsAndConsonants(string.replace(" ", ""), 1)
        case 5:
            splitAndReverseString(string.split(" "))
        case 6:
            index = int(input("Enter index: "))
            print(findWordInString(string.split(" "), index))
        case 7:
            string = askString()
        case _:
            print("I dont know what is an operation...")
    return string

def main():
    userChoice = 1
    stringUser = askString()
    while userChoice != 0:
        showInfo(stringUser)
        userChoice = int(input("Choose an operation to do: "))
        stringUser = chooseFunction(stringUser, userChoice)

main()