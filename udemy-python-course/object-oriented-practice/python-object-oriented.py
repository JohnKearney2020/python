# =====================================================
#                 Dictionary Example
# =====================================================

# my_student = {
#     'name': 'Rolf Smith',
#     'grades': [70, 88, 90, 99]
# }

# def avg_grade(student)
    # avg_list = my_student['grades']
    # print(avg_list)
    # sum = 0
    # for each_score in avg_list:
    #     sum += int(each_score)
    # avg = sum / len(avg_list)
    # print(f'Average score was: {avg}')

#OR

# def avg_grade(student):
#     return sum(student['grades']) / len(student['grades'])
# print(avg_grade(my_student))




# *****************************************************************
#                               Classes
# *****************************************************************

class Student: #classes start with a capital letter
    def __init__(self, new_name, new_grades): #called dunder functions for double underscores
        self.name = new_name
        self.grades = new_grades 

    def average(self):
        return sum(self.grades) / len(self.grades)

#create an object. An object allows us to store data and to store actions
student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])
print(student_one.name)
print(student_two.name)


#      Exercise - your First Python class
     