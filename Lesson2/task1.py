
stringUser = input("Enter your string: ").replace(" ", "").upper()
chars = dict.fromkeys(stringUser, 0)

for char in stringUser:
    chars[char] += 1

for char in chars:
    print(str(char) + ":" + str(chars[char]), end=' ')

print("\n====================")
print(sorted(chars.items())) # sorted by alphabet
print("====================")
print(sorted(chars.items(), key = lambda x: x[1], reverse= True)) # sorted by values of chars