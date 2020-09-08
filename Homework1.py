#Rhahan Sarwar
#1818964
#CIS2348 Homework_1


print('Birthday Calculator')
print('\n')
print('Current Day')

c_month = int(input("Month: "))
if c_month > 12 or c_month < 1:
    print('Invalid month, please input proper month')
    print('\n')
    c_month = int(input("Month: "))

c_day = int(input("Day: "))
if c_day > 31 or c_day < 1:
    print('Please input proper day')
    print('\n')
    c_day = int(input("Day: "))

c_year = int(input("Year: "))
if c_year > 2021 or c_year < 1900:
    print('Please input proper date')
    print('\n')
    c_year = int(input("Year: "))

print('\n')
print('Birthday')

b_month = int(input("Month: "))
if b_month > 12 or b_month < 1:
    print('Invalid month, please input proper month')
    print('\n')
    b_month = int(input("Month: "))

b_day = int(input("Day: "))
if b_day > 31 or b_day < 1:
    print('Please input proper day')
    print('\n')
    b_day = int(input("Day: "))

b_year = int(input("Year: "))
if b_year > 2021 or b_year < 1900:
    print('Please input proper date')
    print('/n')
    b_year = int(input("Year: "))

age_diff = c_year - b_year - 1

if (b_month < c_month):
    age_diff += 1
elif (c_month == b_month):
    if (b_day < c_day):
        age_diff += 1
if (c_month == b_month and b_day == c_day):
    print('Happy Birthday')

print("\n")
print('You are ' + str(age_diff) + ' years old')

