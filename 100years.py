from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))
year_at100 = (date.today().year - age) + 100

print("Hey %s , You will turn 100 years old in %d" % (name, year_at100)) 