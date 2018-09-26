import random
import string
special_characters = '!@#$%^&*~_'
char_set = string.ascii_uppercase + string.digits + string.ascii_lowercase + special_characters
print (''.join(random.sample(char_set*6, 10)))


