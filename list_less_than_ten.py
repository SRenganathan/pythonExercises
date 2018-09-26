list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
number_from_user = int(input("Enter a number:"))
for number in list_one:
    if number<number_from_user:
        new_list.append(number)
print(new_list)
