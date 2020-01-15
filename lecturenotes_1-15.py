# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# #values inside a list are called items
# print(days[5])

# numbers = [1, 2, 3, 4, 5]

# # #print(numbers[:], numbers[3])

# # #print(len(numbers))

# numbers[0] = "20"
# print(numbers)
# numbers.append(40)
# print(numbers)

# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]

# todos.append("binge watch a show")
# todos.append("go to sleep")
# print(todos)

# index = 0
# while index < len(todos):
#     print(f'{index + 1}: {todos[index]}')
#     index += 1

# a = [1, 4, 7, 9, 10]
# b = [4, 6, 8, 9]

# #print(a + b)
# del a[1]
# print(a)

# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]

# to_add = 'placeholder to initialize while loop'
# while (len(to_add) > 0):
#     to_add = input('What item do you want to add to your to-do list?: ')
#     if len(to_add) > 0:
#         todos.append(to_add)
#         print(f'Your current to-do list is: ')
#         print(f'{todos}')
#     else:
#         break
# print('Your final to-do list is: ')
# print(todos)

#more efficient version below
# to_add = input('What item do you want to add to your to-do list?: ')
# while (len(to_add) > 0):
#         todos.append(to_add)
#         print(f'Your current to-do list is: ')
#         print(f'{todos}')
#         to_add = input('What item do you want to add to your to-do list?: ')
# print('Your final to-do list is: ')
# print(todos)

# numbers = [1, 2, 3, 4, 5]
# students = ['a', 'b', 'c', 'd', 'e']
# # print(numbers)
# # numbers.insert(4, 12)
# # print(numbers)
# #numbers.pop(4)
# #print(numbers)
# # while len(numbers)>0:
# #     print(numbers.pop())
# #     print(numbers)
# # print('finished')
# #print(numbers.index(4))
# print(students.index('c'))

# my_num = 3
# my_copy_num = my_num
# my_copy_num = 5
# print(my_num)
# print(my_copy_num)

numbers = [1, 2, 3, 4, 5]
students = ['a', 'b', 'c', 'd', 'e']

# numbers = students.copy()
# print(numbers)

# newlist = numbers + students
# print(newlist)

# print(numbers * 2)

# multi_list = [[7,8], [12,10]]
# print(multi_list[0][0]) # 7
# print(multi_list[0][1]) # 8
# print(multi_list[1][0]) # 12
# print(multi_list[1][1]) # 10

# new_list_sort = [4, 293, 1000, 50, 1, 39]
# new_list_sort.sort()
# print(new_list_sort)

# new_list_sort.extend([1, 2, 3, 567])
# #new_list_sort.append([1, 2, 3, 567])
# print(new_list_sort)

# new_list_sort.clear()
# print(new_list_sort)

# my_string = 'Hello World'

# print(my_string[3])

alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = 0
# while index < len(alphabet):
#     #print(alphabet[index])
#     index += 1

# print(type(alphabet))

# alph2 = list(alphabet)
# print(type(alph2))
# print(alph2)

# alph2_string = " ".join(alph2)
# print(alph2_string)

# my_tupel = (1, 2, 3, 'Hello')
# print(my_tupel)
# print(my_tupel[3])

# pi_1, pi_2, pi_3 = (3.14, 6.28, 9.42)
# print('hello')

# for i in range(0,26,1):
#     print(alphabet[i], end='')
    
# print('')
# for letter in alphabet:
#     print(letter, end='')

# for i in range(1, 1001, 2):
#     print(i, end=", ")

for i in range(1,11,1):
    print('')
    for ii in range(1,11,1):
        print(f'{i} X {ii} = {i*ii}', end=', ')