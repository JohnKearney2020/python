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
#same as above, but done as a Class instead of a dictionary
# class Student: #classes start with a capital letter
#     def __init__(self, new_name, new_grades): #called dunder functions for double underscores
#         self.name = new_name #a variable inside a class is called a property
#         self.grades = new_grades 

#     def average(self):
#         return sum(self.grades) / len(self.grades)

# #create an object. An object allows us to store data and to store actions
# student_one = Student('Rolf Smith', [70, 88, 90, 99])
# student_two = Student('Jose', [50, 60, 99, 100])
# print(student_one.name)
# print(student_two.name)
# print(student_one.average())
# #print(Student.average()) #this will throw an error. We have to call it with an object, or pass in an object like below
# print(Student.average(student_one)) #this will work, but is a little redundant since we've already declared student one as an object, and could just do 
# #student_one.average() instead. However, this is what is going on in the background when we call print(student_one.average())


#-----------------------------------------
#      Exercise - your First Python class
#-----------------------------------------
# class Movie:
#     def __init__(self, new_name, new_director):
#         self.name = new_name
#         self.director = new_director
#     def print_info(self):
#         print(f'<<{self.name}>> by {self.director}')

# movie = Movie('The Matrix', 'Wachowski')
# movie.print_info()

#-----------------------------------------
#      Special Methods
#-----------------------------------------
# movies = ['Matrix', 'Finding Nemo']
# print(movies.__class__) #the Class of Movies is 'list', this list is an object
# print('hi'.__class__) #this is class string

# class Garage:
#     def __init__(self):
#         self.cars = []
#     def __len__(self): #this is necessary for len(ford) to work
#         return len(self.cars)
#     def __getitem__(self, i):
#         return self.cars[i]
#     def __repr__(self): #if only implementing one, implement the repr method. He is strong proponent that any class you create should have a repr and a str method
#         return f'<Garage {self.cars}>'
#     def __str__(self):
#         return f'Garage with {len(self)} cars.'
    

# ford = Garage()
#print(ford.cars)
# ford.cars.append('Fiesta')
# ford.cars.append('Focus')
#print(ford.cars)
#print(len(ford)) #won't work without the method we created above
# print(len(ford.cars)) #this will worl without the method we created above
#print(ford[0]) #another way of calling Garage.__getitem__(ford, 0), this will also print 'Fiesta'
#print(ford.cars[0]) #this will print 'Fiesta'
# print(ford) #this will print the __str__ method we defined above

#-----------------------------------------
#      Iterating over an Object
#-----------------------------------------
#the __getitem__ method  we created above allows you to loop over your object
# for car in ford:
#     print(car)

#-----------------------------------------
#      Exercise - magic methods in Python
#-----------------------------------------
# class Club:
#     def __init__(self, name):
#         self.name = name
#         self.players = []

#     def __len__(self):
#         return len(self.players)

#     def __getitem__(self, i):
#         return self.players[i]

#     def __repr__(self): #if only implementing one, implement the repr method. He is strong proponent that any class you create should have a repr and a str method
#         return f'Club {self.name} with {len(self.players)} players'
#         #return 'Club {}: {}'.format(self.name, self.players)

#     def __str__(self):
#         return f'Club {self.name}: {self.players}'
#         #return 'Club {} with {} players'.format(self.name, len(self))
 

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                 Inheritance
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []
    
#     def average(self):
#         return sum(self.marks) / len(self.marks)

# class WorkingStudent:
#     def __init__(self, name, school, salary):
#         self.name = name
#         self.school = school
#         self.marks = []
#         self.salary = salary
#     def average(self):
#         return sum(self.marks) / len(self.marks)

# rolf = WorkingStudent('Rolf', 'MIT', 15.50)
# print(rolf.salary)
# rolf.marks.append(56)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#This is all well and good, but we can reduce a LOT of the duplication in WorkingStudent
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# class WorkingStudent(Student): #WorkingStudent is a child of Student, it extend student
#     def __init__(self, name, school, salary):
#         #we MUST keep these properties even though they are duplicate from the Student class
#         super().__init__(name, school) #super is the Parent class, itc Student, where we first declared name and school. Since WorkingStudent also takes name and school as
#         #parameters, we need to include those in the parenthesis. We do NOT include marks as that is not a parameter for WorkingStudent
#         self.salary = salary #salary is unique to this class and must be declared like so here
#     #we still have the average method in the WorkingStudent class because we defined it earlier in the Student class and we set WorkingStudent up to inherit Student
#     def weekly_salary(self):
#         return self.salary*40

# rolf = WorkingStudent('Rolf', 'MIT', 15.50)
# print(rolf.salary)
# rolf.marks.append(57)
# rolf.marks.append(99)
# print(rolf.average())
# print(rolf.weekly_salary())

#classes flow down hill. The parent does not get the functionality of its children. However, the children do get the functionality of their parents.



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                 The @ property
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#if a method is ***NOT*** performing actions (connecting to a database, for example), and is simply performing calculations and
#returning a value, we can use the @property to simplify the method call

# class Student:
#     def __init__(self, name, school):
#         self.name = name
#         self.school = school
#         self.marks = []
    
#     def average(self):
#         return sum(self.marks) / len(self.marks)

# class WorkingStudent(Student): #WorkingStudent is a child of Student, it extend student
#     def __init__(self, name, school, salary):
#         #we MUST keep these properties even though they are duplicate from the Student class
#         super().__init__(name, school) #super is the Parent class, itc Student, where we first declared name and school. Since WorkingStudent also takes name and school as
#         #parameters, we need to include those in the parenthesis. We do NOT include marks as that is not a parameter for WorkingStudent
#         self.salary = salary #salary is unique to this class and must be declared like so here
#     #we still have the average method in the WorkingStudent class because we defined it earlier in the Student class and we set WorkingStudent up to inherit Student
#     @property
#     def weekly_salary(self):
#         return self.salary*40

# #with the @property, we can use .weekly_salary INSTEAD of .weekly_salary()
# rolf = WorkingStudent('Rolf', 'MIT', 15.50)
# print(rolf.weekly_salary)
# # print(rolf.weekly_salary())