from math import sqrt

userA = int(input("Enter a, b, c to obtain a quadratic equation of the form: ax^2+bx+c=0: \n"))
userB = int(input())
userC = int(input())

print("Your quadratic equation is: ", str(userA) + 'x^2+'+ str(userB) + 'x+' + str(userC) + '=0')
discriminator = (userB**2) - (4*userA*userC)

if discriminator < 0:
    print("There are no roots, cause discriminator < 0")
else:
    discriminator = sqrt(discriminator)
    print("Discriminator =", discriminator)
    if discriminator > 0:
        firstRoot = (-userB+discriminator)/(2*userA)
        secondRoot = (-userB-discriminator)/(2*userA)
    elif discriminator == 0:
        firstRoot = (-userB+discriminator)/(2*userA)
        secondRoot = str("There is no second root.")
    print("First root x1 =", firstRoot,"\nSecond root x2 =", secondRoot)