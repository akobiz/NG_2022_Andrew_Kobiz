lst = input("Enter numbers separated by comma: ").split(",")
sum = 0
print("Max elem = " + max(lst))
lst.remove(max(lst))
print("Min elem = " + min(lst))
lst.remove(min(lst))

print("List without max/min elements: ", lst)

for elem in lst:
    sum += int(elem)

print("Sum of all numbers = " + str(sum))