num1 = int(input("Type first number:"))
num2 = int(input("Type second number:"))
if num1 > num2:
    print(str(num1) + " is bigger than " + str(num2))
elif num2 > num1:
    print(str(num2) + " is bigger than " + str(num1))
else:
    print("Both numbers are equal")