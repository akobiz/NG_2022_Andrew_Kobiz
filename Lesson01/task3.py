import datetime

userSeconds = int(input("Enter a seconds: "))

print("Your date:", datetime.datetime.fromtimestamp(userSeconds))
