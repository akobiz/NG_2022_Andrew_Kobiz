
userSeconds = int(input("Enter a seconds: "))
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

years =  int(userSeconds / 31536000) + 1970 # unixtime / seconds in 1 year
years = int((years - 1969) / 4) # found extra days (leap years)

days = int(userSeconds / 86400) # unixtime / seconds in 24 hrs
secondsCurrentDay = userSeconds -   (days*86400)
hours = int(secondsCurrentDay/3600) # found hours considering my time zone (+3)
minutes = (secondsCurrentDay - hours * 3600) / 60
seconds = int((minutes * 60) - (int(minutes) * 60))
days = (days - years) % 365 # found how much days is gone in this year

for i in range(len(daysInMonth)):
    if days < 31:
        days += 1
        break
    days -= daysInMonth[i]

if hours == 0:
    print("Day",days,":", hours,":" ,int(minutes),":", seconds,".")
else:
    print("Day",days,":", hours + 3,":" ,int(minutes),":", seconds,".")
