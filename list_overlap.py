list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 11, 12, 13]

common_numbers = []

for i in list_two:
    if i in list_one:
        common_numbers.append(i)

print("The list containing the common numbers are :", common_numbers)

