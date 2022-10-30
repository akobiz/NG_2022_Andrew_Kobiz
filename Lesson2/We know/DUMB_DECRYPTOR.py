alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!,.-\" "
cracker = "NOPQRSTUVWXYZABCDEFGHIJMLK!,.-\" "
cryptedString = input("Enter your shiphered syntance: ")
decryptedString = []

for i in range(0, len(cryptedString)):
    for j in range(0, len(cracker)):
        if cryptedString[i].upper() == cracker[j].upper():
            decryptedString.append(alphabet[j])
    
for char in decryptedString:
    print(char, end='')
