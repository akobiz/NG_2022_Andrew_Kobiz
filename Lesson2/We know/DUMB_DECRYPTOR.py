from dev_log import *

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!,.-\" "
cracker = "NOPQRSTUVWXYZABCDEFGHIJMLK!,.-\" "
cryptedString = input("Enter your shiphered syntance: ")
decryptedString = []

for i in range(0, len(cryptedString)):
    for j in range(0, len(cracker)):
        if cryptedString[i].upper() == cracker[j].upper():
            info("IF is working...")
            decryptedString.append(alphabet[j])
  #      elif cryptedString[i] == "!" or cryptedString[i] == "," or cryptedString == " " or cryptedString == "," and decryptedString[:-1] !=  cryptedString[i]:
   #         info("Elif")
   #         decryptedString.append(cryptedString[i])
            
for char in decryptedString:
    print(char, end='')
