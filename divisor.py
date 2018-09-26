number_from_user = int(input("Enter a number:"))
divisor_list = []
for i in range(2,(int(number_from_user/2)+1)):
    if (number_from_user%i == 0):
        divisor_list.append(i)
print("The list of divisors for the number %d excluding 1 are: " % number_from_user)
print(divisor_list," and of course, %d" % number_from_user)
