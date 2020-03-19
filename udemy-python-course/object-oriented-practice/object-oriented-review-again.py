# class Student:
#     def __init__(self, new_name, new_grade):
#         self.name = new_name
#         self.grades = new_grade
    
#     def average(self):
#         return sum(self.grades) / len(self.grades)

# student_one = Student('John Kearney', [97, 99, 88, 78, 100])
# student_two = Student('Jose', [50, 60, 99, 100])
# #print(student_one.name)
# #print(student_one.grades[0])
# print(student_one.average())

# class Movie:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

# matrix = Movie('The Matrix', 1994)
# print(matrix.name)
# #print(Movie('The Matrix', 1994).name)

#first exercise
# class Movie:
#     def __init__(self, name, director):
#         self.name = name
#         self.director = director
#     def print_info(self):
#         print(f'<<{self.name}>> by {self.director}')

# class Student:
#     def __init__(self, name):
#         self.name = name

# movies = ['Matrix', 'Findind Nemo']
# print(movies.__class__)





#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                               Additional Dunder Methods
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# class Garage:
#     def __init__(self):
#         self.cars = []
#     def __len__(self):
#         return len(self.cars)
#     def __getitem__(self, i): #this allows us to easily loop over our object
#         #NOTE: this is hard coded to getitem. If you were to change it to getitems, it will not work
#         return self.cars[i]
#     def __repr__(self): #this is a more 'code oriented' description
#         #should be used to return a string that represents the object. 
#         #This can be good for debugging. Use this one over the __str__ method if you need to choose between them
#         return f'<Garage {self.cars}'
#     def __str__(self):
#         return f'Garage with {len(self)} cars.' #this is a more user-oriented description of our code
#         #this calls the __len__ method above
#         #this would trigger if the user did print(ford), for example

# ford = Garage()
# ford.cars.append('Fiesta')
# ford.cars.append('Focus')

# print(len(ford)) #this is possible b/c of the __len__ method above
# print(len(ford.cars)) #this prints the saem thing, and will work without the __len__ method above

# print(ford[0]) #the def __getitem__ method allows this to work
# print(ford.cars[0])# this prints out the same thing as the item above

# for car in ford: #this is possible because of the __getitem__ method above
#     print(car)
# for car in ford.cars: #this prints the same thing
#     print(car)

#print(ford) #will print the __str__ method if present, otherwise the __repr__ method



#Exercise #2
# class Club:
#     def __init__(self, name):
#         self.name = name
#         self.players = []
#     def __getitem__(self, i):
#         return self.players[i]
#     def __len__(self):
#         return len(self.players)
#     def __repr__(self):
#         return 'Club {club_name}: {list_o_players}'.format(club_name = self.name, list_o_players = self.players)
#     def __str__(self):
#         return 'Club {club_name} with {count_of_players} players'.format(club_name = self.name, count_of_players = len(self))

# arsenal = Club('Arsenal')



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                               Inheritance
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary): #need to keep name and school even though they are repeats from the earlier Student method
        super().__init__(name, school) #this calls the __init__ method in the parent class, the Student class above, and it initializes name and school
        self.salary = salary #salary is the only unique variable that needs to be initialized in this class
    
    @property #don't use this for actions, such as connecting to a database, only use it for calculations.
    def weekly_salary(self):
        return self.salary * 40
        
rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.salary)
print(rolf.weekly_salary) #don't need the () because of the @property decorator
