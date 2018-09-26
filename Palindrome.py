user_input = str(input("Enter a string:")).lower()
string_length = len(user_input)
for i in range(0,int(string_length/2)):
    if (user_input[i] != user_input[string_length-i-1]):
        print(user_input, " is not a palindrome!")
        break
    else:
        print("Checking digit %d, So far positive, But I still have to check. Please wait..." %i)
        if(i == int(string_length/2)-1):
            print(user_input.title(), "is a palindrome, Yay :)")
        