import random
import string

print("This program will generate a password with random characters")
print("Enter the password difficulty:")

user_difficulty = input("Type H for Hard, M for Medium and W for a weak password: ")
number_of_digits = int(input("Enter the length of the password:"))

if (user_difficulty == 'H'):
    special_characters = '!@#$%^&*~_'
    char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_characters
    print (''.join(random.sample(char_set*6, number_of_digits)))
elif (user_difficulty == 'M'):
    special_characters = '!@#$'
    char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_characters
    print (''.join(random.sample(char_set*6, number_of_digits)))
else:
    char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase 
    print (''.join(random.sample(char_set*6, number_of_digits)))
