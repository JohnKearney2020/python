# =====================================================================================
# Medium PROBLEMS
# =====================================================================================

# ============================
# 1 - Find the smallest number
# ============================
# number_list = [456, 23, 100, 4567, 223, 89, 234, 45, 6, 135]
# def smallest_number(number_list):
#     smallest = number_list[0]
#     for each_number in number_list:
#         if each_number < smallest:
#             smallest = each_number
#     return smallest
# print(f'Your list is: {number_list}')
# print(f'The smallest number in your list is: {smallest_number(number_list)}')

# ============================
# 2 - Find the largest number
# ============================
# number_list = [456, 23, 100, 4567, 223, 89, 234, 45, 6, 135]
# def largest_number(number_list):
#     largest = number_list[0]
#     for each_number in number_list:
#         if each_number > largest:
#             largest = each_number
#     return largest
# print(f'Your list is: {number_list}')
# print(f'The largest number in your list is: {largest_number(number_list)}')

# ============================
# 3 - Find the shortest String
# ============================
# list_o_strings = ['hello', 'goodbye', 'Kearney', 'let\'s go!', 'Ohio State', 'more', 'lesson', 'help!']
# def shortest(string_list):
#     shortest_str = string_list[0]
#     for each_string in string_list:
#         string_len = len(each_string)
#         if string_len < len(shortest_str):
#             shortest_str = each_string
            
#     return shortest_str
# print(f'Your list of strings is: {list_o_strings}')
# print(f'The shortest string in your list is: {shortest(list_o_strings)}')

# ============================
# 4 - Find the longest String
# ============================
# list_o_strings = ['hello', 'goodbye', 'Kearney', 'let\'s go!', 'Ohio State', 'more', 'lesson', 'help!']
# def longest(string_list):
#     longest_str = string_list[0]
#     for each_string in string_list:
#         string_len = len(each_string)
#         if string_len > len(longest_str):
#             longest_str = each_string            
#     return longest_str
# print(f'Your list of strings is: {list_o_strings}')
# print(f'The shortest string in your list is: {longest(list_o_strings)}')

# =====================================================================================
# LARGE PROBLEMS
# =====================================================================================

# ============================
# 1 - Tic-tac-toe
# ============================
#def move(board, location, player):

board = [['-','-','-'],['-','-','-'],['-','-','-']] # 3 x 3 matrix representing our board
location = []

#Get player value
player = input('Do you want to be player X or player Y?: ')
player = player.upper()
while player != 'X' and player != 'Y':
    player = input('Type X or Y to choose your player: ')
    player = player.upper()

#get location
print('Choose a location to place your \'X\' or \'O\' in the form of "column, row: "')
print('For example, if you type '1,1' without the \'\')
location = input('Choose a location to place your \'X\' or \'O\' in the form of "column, row" without the "": ')
print(location)




# =====================================================================================
# SMALL PROBLEMS
# =====================================================================================

# ====================
# 1  - Madlib function
# ====================

# def madlib(name='OMITTED', subject='OMITTED'):
#     return f'{name}\'s favorite subject is {subject}.'
# print(madlib('John', 'Fluid Mechanics'))
# print(madlib())

# ====================================
# 2 - Celsius to Fahrenheit conversion
# ====================================

# def C_to_F(degC):
#     degF = (degC * 9/5 + 32)
#     return degF
# print(f'{C_to_F(100):.2f}')
# print(f'{C_to_F(0):.2f}')

# ====================================
# 3 - Fahrenheit to Celsius conversion
# ====================================

# def F_to_C(degF):
#     degC = (degF - 32) * (5/9)
#     return degC
# print(f'{F_to_C(100):.2f}')#:.2f prints a float to two decimal places
# print(f'{F_to_C(0):.2f}')

# ====================
# 4 - is_even function
# ====================

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(f'Is {12} even?: {is_even(12)}')
# print(f'Is {17} even?: {is_even(17)}')

# ====================
# 5- is_odd function
# ====================

# def is_odd(num):
#     even_val = is_even(num)
#     if even_val == True:
#         return False
#     else:
#         return True

# print(f'Is {12} odd?: {is_odd(12)}')
# print(f'Is {17} odd?: {is_odd(17)}')

# ======================
# 6- only_evens function
# ======================
# number_list = [11, 20, 42, 97, 23, 10]
# def only_evens(number_list):
#     list_of_evens = []
#     for each_number in number_list:
#         if each_number % 2 == 0:
#             list_of_evens.append(each_number)
#     return list_of_evens
# print(f'Your original list: {number_list}')
# print(f'Same list with only evens: {only_evens(number_list)}')

# ======================
# 7- only_odds function
# ======================
# number_list = [11, 20, 42, 97, 23, 10]
# def only_evens(number_list):
#     list_of_odds = []
#     for each_number in number_list:
#         if each_number % 2 != 0:
#             list_of_odds.append(each_number)
#     return list_of_odds
# print(f'Your original list: {number_list}')
# print(f'Same list with only odds: {only_evens(number_list)}')


