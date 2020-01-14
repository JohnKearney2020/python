# ===============================================
# Medium
# ===============================================
#1 tip calculator
total_bill = int(input('What was your total bill? Do not include the dollar sign: '))
level_of_service = input('What was your level of service? Choose good/fair/bad: ')

if level_of_service == 'good':
    tip_amount = total_bill * .20
    total_amount = total_bill * 1.20
    print(f'Tip Amount: ${tip_amount}')
    print(f'Total Amount: ${total_amount}')
elif level_of_service == 'fair':
    tip_amount = total_bill * .15
    total_amount = total_bill * 1.15
    print(f'Tip Amount: ${tip_amount}')
    print(f'Total Amount: ${total_amount}')
elif level_of_service == 'fair':
    tip_amount = total_bill * .10
    total_amount = total_bill * 1.10
    print(f'Tip Amount: ${tip_amount}')
    print(f'Total Amount: ${total_amount}')
else:
    print("Try again, make sure to choose good, fair, or bad.")

print(f'Tip amount: {tip_amount}')
#test
print("test")

# ===============================================
# SMALL
# ===============================================

#1
# name = input('What is your name?: ')
# print(f'Hello, {name}!')

#2
# name = input('What is your name?: ')
# name = name.upper()
# print(f'HELLO, {name}!')
# name_len = len(name)
# print(f'YOUR NAME HAS {name_len} LETTERS IN IT! AWESOME!')

#3
# print('Please fill in the blanks below:')
# print('___(name)___\'s favorite food in the whole world is ___(food)___.')
# name = input('Username: ')
# food = input('Food: ')
# print(f'{name}\'s favorite food in the whole world is {food}.')

#4
# day_int = int(input('Input a day of the week. 0 for Sunday, 6 for Saturday: '))
# if day_int == 0:
#     print("Sunday")
# elif day_int == 1:
#     print("Monday")
# elif day_int == 2:
#     print("Tuesday")
# elif day_int == 3:
#     print("Wednesday")
# elif day_int == 4:
#     print("Thursday")
# elif day_int == 5:
#     print("Friday")
# else:
#     print("Saturday")

#5
# day_int = int(input('Input a day of the week. 0 for Sunday, 6 for Saturday: '))
# if day_int == 0 or day_int == 6:
#     print('Sleep in!')
# else:
#     print('Go to work :(')

#6
# def degC_to_degF(degC):
#     degF = (degC*(9/5)) + 32
#     return degF

# degC = int(input('Enter a temp in Celsius: '))
# print(f'{degC} Celsius is {degC_to_degF(degC)} Fahrenheit.')

#7
# counter = 0
# while (counter < 10):
#     counter += 1
#     print(counter)

#8
# num_start = int(input('Choose a number to start from: '))
# num_end = int(input('Choose a number to end on: '))

# if num_end <= num_start:
#     print('Your ending number must be larger than your starting number!')
# else:
#     while num_start <= num_end:
#         print(num_start)
#         num_start += 1

#9
# print('''@@@@@
# @@@@@
# @@@@@
# @@@@@
# @@@@@''')

#10
# user_n = int(input('Choose a number for your N x N square: '))
# counter = 0
# row_string = '@' * user_n
# while counter <= user_n:
#     counter += 1
#     print(row_string)


