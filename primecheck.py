user_number = int(input("Enter a number: "))

def is_prime_or_not(number_from_user):
    divisor_list = []
    for i in range(2,(int(number_from_user/2)+1)):
        if (number_from_user%i == 0):
            divisor_list.append(i)
    if not divisor_list:
        return("%d is a prime number" %number_from_user)
    else:
        return("%d is not a prime number" %number_from_user)

print(is_prime_or_not(user_number))


