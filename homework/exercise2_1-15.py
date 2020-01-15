# ====================================================================
# Medium Problems
# ====================================================================

# =====================
# 1 - Multiply Vectors
# =====================
# vector_1 = [2, 4, 5]
# vector_2 = [2, 3, 6]
# multiplied_vector_list = []
# for i in range(0, len(vector_1),1):
#     vector_1_val = vector_1[i]
#     vector_2_val = vector_2[i]
#     multiplied_vector_list.append(vector_1_val * vector_2_val)
# print(f'Your new vector list is: {multiplied_vector_list}')

# =====================
# 2 - Matrix Addition
# =====================
#this is the TA's solution he shared. I rewrote it in a way I understand a lot better in
#part II of this
# a = [[1,3], [2,4]]
# b = [[5,2], [1,0]]
# new_big_list = []
# # outer
# for indexOne in range(len(a)):
#     # a[index] b[index]
#     # [1,3]       [5, 2]
#     new_small_list = []
#     # inner
#     for indexTwo in range(len(a[indexOne])):
#     #for indexTwo in range(len(a)):
#         sum_of_values = a[indexOne][indexTwo] + b[indexOne][indexTwo]
#         new_small_list.append(sum_of_values)
#     new_big_list.append(new_small_list)
# print(new_big_list)

# =======================
# 3 - Matrix Addition II
# =======================

#Think of this as the 3 Dimensional matrix these lists represent, with rows and columns!
#list_1 = [['a','b','c'],['d','e','f'],['g','h','i']]
#list_2 = [['A','B','C'],['D','E','F'],['G','H','I']]
#list_1 = [[1,3],[2,4]]
#list_2 = [[5,2],[1,0]]
#list_1 = [[2,4], [1,6]]
#list_2 = [[4,7], [2,3]]
# list_1 = [[1,2,3],[1,2,3],[1,2,3]]
# list_2 = [[1,2,3],[1,2,3],[1,2,3]]
# final_added_matrix = []
# row_for_final_matrix = []
# for column in range(len(list_1[0])): #list_1[0] is [a,b,c], the first item in list_1, and getting its length is equivalent
#     #to counting the number of rows we have in our 3 Dimensional matrix
#     #print('stuff')
#     row_for_final_matrix = [] #need to reset this to be blank with each iteration
#     for row in range(len(list_1)): #len(list_1) is the "height", or the number of rows in our 3D matrix
#         #we now have a column and row value, and get "coordinates" for each value in our matrix
#         list_1_value = list_1[column][row] 
#         list_2_value = list_2[column][row]
#         row_for_final_matrix.append(list_1_value + list_2_value)
#     final_added_matrix.append(row_for_final_matrix)
# print(final_added_matrix) 

# ======================
# 4 - De-dup
# ======================
list_of_numbers = [1, 33, 23, 6, 8, 33, 1, 11, 67, 100, 6]
duplicate_check = []
new_list_sans_dups = []
for number in list_of_numbers:
    is_duplicate = False #needs to be reset here on each loop
    for dup_number in duplicate_check:
        if number == dup_number:
            is_duplicate = True
            break #exit this loop if it is indeed a duplicate we've already accounted for       
    if is_duplicate == True:
        continue #if a duplicate, go to the next number in list_of_numbers
    else:
        duplicate_check.append(number) # add it to our duplicate list so we'll catch it in the future
        new_list_sans_dups.append(number)
print(new_list_sans_dups)
    



# ====================================================================
# Small Problems
# ====================================================================

# =============
# 1 - sum list
# =============
# num_list = [1, 34, 5, 12, 2]
# sum = 0
# for i in range(0, len(num_list),1):
#     sum += num_list[i]
# print(sum)

#====================
# 2 - largest number
#====================
# num_list = [1, 34, 333, 221, 73, 69, 6]
# largest_num = num_list[0]
# for number in num_list:
#     if number > largest_num:
#         largest_num = number
# print(f'Largest number is: {largest_num}')

#====================
# 3 - smallest number
#====================
# num_list = [45, 34, 333, 221, 73, 69, 6]
# smallest_num = num_list[0]
# for number in num_list:
#     if number < smallest_num:
#         smallest_num = number
# print(f'Your smallest number is: {smallest_num}.')

#==================
# 4 - Even Numbers
#==================
# num_list = [45, 34, 333, 221, 1000, 73, 69, 6, 122]
# for number in num_list:
#     if number % 2 == 0:
#         print(f'Even number from list: {number}')

#======================
# 5 - Positive Numbers
#======================
# num_list = [45, -34, 333, -221, 1000, 73, -69, -6, 122]
# for number in num_list:
#     if number > 0:
#         print(f'Positive number from list: {number}')

#========================
# 6 - Positive Numbers II
#========================
# num_list = [45, -34, 333, -221, 1000, 73, -69, -6, 122]
# positive_numbers = []
# for number in num_list:
#     if number > 0:
#         #print(f'Positive number from list: {number}')
#         positive_numbers.append(number)
# print('Your list of positive numbers is: ')
# print(positive_numbers)

#========================
# 7 - Multiply a list
#========================
# num_list = [45, -34, 333, -221, 1000, 73, -69, -6, 122]
# multi_factor = 2
# multiplied_list = []
# for number in num_list:
#     multiplied_list.append(multi_factor * number)
# print('Your list of multiplied numbers is: ')
# print(multiplied_list)

#========================
# 8 - Reverse a String
#========================
# my_string = 'John Kearney'
# reversed_string = ''
# for i in range(len(my_string) - 1, -1, -1):
#     reversed_string += my_string[i]
# print(f'Your reversed string is: {reversed_string}')

