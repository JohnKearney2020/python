# students = ['matt', 'forkhan', 'alex', 'mary']
# for each_student in students:
#     print(each_student, end= ' ')

# weeks = ['WEEK 1: Command Line, Git, Python', 'WEEK 2: Python', 'WEEK 3: Front-End Foundations', 'WEEK 4: Javascript', 'WEEK 5: Javascript']
# days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# day_description = ['Lecture:', 'Homework:', 'Solutions:']
# for each_week in weeks:
#     print(each_week)
#     for each_day in days:
#         print(f'\t{each_day}')
#         for each_bullet_point in day_description:
#            print(f'\t\t{each_bullet_point}') 

# def print_students():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print_students()
# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print_students()
# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print_students()

# def greeting(person):
#     print(f'Hello, {person}.')

# greeting('John')

# def add(num1, num2):
#     return num1 + num2
#     #return 'hello'
# result = add(4,5)
# print(result)

# def concat_lists(list1, list2):
#     concat = list1 + list2
#     return concat

# print(concat_lists([1,3,4],[5,2,4]))
# def cal_avg(param1, param2, param3, param4):
#     sum = param1 + param2 + param3 + param4
#     avg = sum / 4
#     return avg
# result = cal_avg(4, 6, 10, 16)
# print(result)

# def cal_avg2(list_of_nums):
#     sum = 0
#     for each_number in list_of_nums:
#         sum += each_number
#     avg = sum / len(list_of_nums)
#     return avg
# nums = [25, 6, 7, 2, 3, 35, 8, 90]

# result = cal_avg2(nums)
# print(result)

# def my_function(num1, num2, num3):
    
#     return num1*2, num2*3, num3*4

# result = my_function(4, 7, 9)
# one, two, three = my_function(4, 7, 9)
# print(result)
# print(one)
# print(two)
# print(three)

# print('Hello')
# def greeting(name):
#     print(f'hello {name}')

# students = ['Kazim', 'Matt', 'Alina', 'Mary']
# for name in students:
#     greeting(name)
# print('bye')

TAX_RATE = .09  # 9 percent tax
COST_PER_SMALL_WIDGET = 5.00
COST_PER_LARGE_WIDGET = 8.00
def calculateCost(nSmallWidgets, nLargeWidgets):
    subTotal = (nSmallWidgets * COST_PER_SMALL_WIDGET) + (nLargeWidgets * COST_PER_LARGE_WIDGET)
    taxAmount = subTotal * TAX_RATE
    totalCost = subTotal + taxAmount
    return totalCost
total1 = calculateCost(4, 8)  #  4 small and 8 large widgets
print('Total for first order is', total1)
total2 = calculateCost(12, 15)