import datetime

userSeconds = int(input("Enter a seconds: "))
resDate = str(datetime.datetime.fromtimestamp(userSeconds))

print("Your date:", resDate.replace(" ",":")[8:])