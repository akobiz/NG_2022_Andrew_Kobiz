def askString():
    return input("Enter your string: ")

def recursionCounting(dictionary, string, count = 0):
    if count == len(dictionary):
        return 0
    keyList = list(dictionary)
    dictionary[keyList[count]] = string.count(keyList[count])
    return recursionCounting(dictionary, string, count + 1)

string = askString().replace(" ", "")
dictionary = dict.fromkeys(string, 0)
recursionCounting(dictionary, string, 0)
print(dictionary)
