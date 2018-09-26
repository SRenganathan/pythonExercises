
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if (number1%number2 == 0):
    print("%d is divisible by %d" % (number1,number2))
else:
    print("%d is not divisible by %d" % (number1,number2))