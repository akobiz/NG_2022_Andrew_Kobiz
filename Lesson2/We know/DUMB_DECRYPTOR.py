alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!,.-\" "
cracker = "NOPQRSTUVWXYZABCDEFGHIJMLK!,.-\" "
cryptedString = input("Enter your shiphered syntance: ")
decryptedString = []

for shiphredChar in range(0, len(cryptedString)):
    for decryptorChar in range(0, len(cracker)):
        if cryptedString[shiphredChar].upper() == cracker[decryptorChar].upper():
            decryptedString.append(alphabet[decryptorChar])
    
for char in decryptedString:
    print(char, end='')
