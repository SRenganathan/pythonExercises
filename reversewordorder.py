user_string = input("Enter a long string containing multiple words:")

def reverse_word_order(user_string):
    result = user_string.split(" ")
    count = len(result)-1
    new_word = []
    for i in range(len(result)):
        new_word.append(result[count])
        count -= 1
    reversed_word = " ".join(new_word)
    return(reversed_word)

print(reverse_word_order(user_string))

