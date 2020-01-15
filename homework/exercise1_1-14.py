# =====================================================================================================
# Medium Problems
# =====================================================================================================
#==================
# 1 tip calculator
#==================
# total_bill = float(input('What was your total bill? Do not include the dollar sign: '))
# level_of_service = input('What was your level of service? Choose good/fair/bad: ')


# if level_of_service == 'good':
#     tip_amount = total_bill * .20100
#     total_amount = total_bill * 1.20
#     #print(f'Tip Amount: ${tip_amount:.2f}') # :.2f is the newer version of "%.2f"
#     #print(f'Total Amount: ${total_amount:.2f}')
# elif level_of_service == 'fair':
#     tip_amount = total_bill * .15
#     total_amount = total_bill * 1.15
#     #print(f'Tip Amount: ${tip_amount:.2f}')
#     #print(f'Total Amount: ${total_amount:.2f}')
# elif level_of_service == 'bad':
#     tip_amount = total_bill * .10
#     total_amount = total_bill * 1.10
#     #print(f'Tip Amount: ${tip_amount:.2f}')
#     #print(f'Total Amount: ${total_amount:.2f}')
# else:
#     print("Try again, make sure to choose good, fair, or bad.")

# print(f'Tip Amount: ${tip_amount:.2f}')
# print(f'Total Amount: ${total_amount:.2f}')

#==================
#2 tip calculator 2
#==================
# total_bill = float(input('What was your total bill? Do not include the dollar sign: '))
# split_num = int(input('How many people will be splitting the check?: ' ))
# level_of_service = input('What was your level of service? Choose good/fair/bad: ')


# if level_of_service == 'good':
#     tip_amount = total_bill * .20
#     total_amount = total_bill * 1.20
# elif level_of_service == 'fair':
#     tip_amount = total_bill * .15
#     total_amount = total_bill * 1.15
# elif level_of_service == 'bad':
#     tip_amount = total_bill * .10
#     total_amount = total_bill * 1.10
# else:
#     print("Try again, make sure to choose good, fair, or bad.")

# print(f'Tip Amount: ${tip_amount:.2f}') # :.2f is the newer version of "%.2f"
# print(f'Total Amount: ${total_amount:.2f}')
# print(f'Amount per person: ${total_amount/split_num:.2f}')

#==================
#3 how many coins
#==================

# num_of_coins = 0
# print(f'You have {num_of_coins} coins.')
# want = input("Do you want another? (Yes/No): ")
# want = want.lower()

# while want != 'no':
#     num_of_coins += 1
#     print(f'You have {num_of_coins} coins.')
#     want = input("Do you want another? (yes/no): ")

#==================
#4 Print a box
#==================
# width = int(input('width?: '))
# height = int(input('Height?: '))
# top_bottom_row_string = '*' * width
# middle_row_blanks = ' ' * (width - 2)
# middle_row = '*' + middle_row_blanks + '*'

# if width > 2 and height > 2:
#     print(top_bottom_row_string)
#     row_counter = 1
#     while row_counter <= height - 2:
#         row_counter += 1
#         print(middle_row)
#     print(top_bottom_row_string)
# else:
#     print(f'Your width and height each need to be greater than 2.')

#==================
#5 Print a Triangle
#==================
# print('   *   ')
# print('  ***  ')
# print(' ***** ')
# print('*******')

#======================
#6 Multiplication Table
#======================
# left_num = 1
# right_num = 1

# while right_num <= 10:
#         #print(f'{left_num} X {right_num} = ' + str(left_num * right_num))
#         print(f'{left_num} X {right_num} = ' + str(left_num * right_num))
#         right_num += 1
#         if right_num == 11:
#             right_num = 1
#             left_num += 1
#             if left_num == 11:
#                 break



# =====================================================================================================
# Large Problems
# =====================================================================================================

#======================
#1 Triangle Numbers
#======================
# number_n = 1
# counter = 1
# while counter <= 100:
#     triangle_number = int(number_n*(number_n + 1)/2)
#     print(f'Triangle Number {counter} is {triangle_number}')
#     counter += 1
#     number_n += 1

#======================
#2 Factor a Number
#======================
# num_to_factor = int(input("Find the factors of the following positive integer: "))
# print(f'The factors of {num_to_factor} are:')
# count_for_division = 1
# while count_for_division <= num_to_factor:
#     even_check = num_to_factor % count_for_division
#     if even_check == 0:
#         print(f'{count_for_division}')
#     count_for_division += 1

#======================
#3 Guess a Number
#======================
# import random
# number_to_guess = random.randint(1, 10)
# guess_count = 0

# print('I am thinking of a number between 1 and 10.')
# number_guessed = int(input('What\'s the number? You get 5 guesses: '))
# while number_guessed != number_to_guess:
#     guess_count += 1
#     if number_guessed < number_to_guess:
#         print("You guessed too low!")
#     elif number_guessed > number_to_guess:
#         print("You guessed too high!")

#     if guess_count == 5:
#         print('You ran out of guesses, noob!')
#         break
#     print(f'You have {5 - guess_count} guesses left.')
#     number_guessed = int(input('What\'s the number?: '))
#     if number_guessed == number_to_guess:
#         print('You win!')
#         break




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


