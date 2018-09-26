a = [5, 10, 15, 20, 25]

def function_for_first_and_last(user_list):
    new_list = []
    new_list.append(user_list[0])
    new_list.append(user_list[len(user_list)-1])
    return(new_list)

operated_list = function_for_first_and_last(a)
print(operated_list)