def pyTheorem(a,b,c):
    equals_C_squared = False
    if (a**2 + b**2 == c**2):
        return True
    else:
        return False
import random

# a = 3
# b = 4
# c = 5
# #equals_C_squared = False

# while (a != -1):
#     # a = random.randint(1, 1000)
#     # b = random.randint(1, 1000)
#     # c = random.randint(1, 1000)
#     # looks like we can't use a randomly generated variable as the limit on our randint(1, limit) method
#     # a = random.randint(1, 1000)
#     # a2 = 1000 - a
#     # b = random.randint(1, a2)
#     # c = 1000 - a - b
#     # a = 200 
#     # b = 375 
#     # c = 425

#     if pyTheorem(a,b,c) == True:
#         if a + b + c == 1000:
#             print(f'a = {a} + b = {b} + {c} = 1000')
#             print(f'and {a}^2 + {b}^2 = {c}^2')
#             print(f'The product a*b*c = {a * b * c}')
#             break
# print('finished')








# string1 = 'aaabbcdd'
# string2 = 'abdbacade'
# duplicates = []

# for each_letter_S1 in string1:
#     if each_letter_S1 in duplicates:
#         continue #skip letters we have already found that match between the two strings
#     for each_letter_S2 in string2:
#         if each_letter_S1 == each_letter_S2:
#             duplicates.append(each_letter_S1)
#             break

# for each_letter_S2 in string2:
#     if each_letter_S2 in duplicates:
#         continue #skip any letters we alre
#     else:
#         print(f'{each_letter_S2} is the unique letter in string 2: {string2}')
#         break
# for each_letter2 in string2:
#     if each_letter2 in string1:
#         pass
#     else:
#         print(f'the unique letter in string 2 is {each_letter2}')
#         break


# def check_triplet(a, b, c):
#     return (a**2) + (b**2) == (c**2)
# limit = 1000
# for x in range(1, 1001):
#     for y in range(x+1, 1001):
#         z = limit - (x + y)
#         if(check_triplet(x, y, z)):
#             if x + y + z == limit:
#                 print(x)
#                 print(y)
#                 print(z)
#                 print(x * y * z)
#                 break