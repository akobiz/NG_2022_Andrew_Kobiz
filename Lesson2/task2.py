strg = str(input("Enter the list separated by commas: ").replace(" ", ""))
lst = strg.split(",")
print (lst)
uniqueValue = set(lst)
print(str(uniqueValue))