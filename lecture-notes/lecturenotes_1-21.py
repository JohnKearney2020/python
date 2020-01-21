# ===================================================================
#                          CLASSES
# ===================================================================
#A class is a containter that can hold a bunch of stuff inside of it.
#class Greeting:
#     def say_hello(self): #self if a placeholder, #self is basically a pointer that is used to differentiate each object that uses a class
#         print('Hello there!')

# # class Person:
# #     #a method is just a function inside of a class

# newGreetingObj = Greeting() #greeting is the class, newGreetingObj is the object

# newGreetingObj.say_hello() #now we call the function

# ==========================================
#               Students class
# ==========================================
class Student:
    def __init__(self, name, lname): #this is a constructor. Constructors are always called when an object is created.
        self.name = name #this is called an instance variable
        self.lname = lname
        #usually you do NOT return from a constructor
        #print('constructor called')
    def greeting(self):
        print('Good morning!')

Alina = Student('Alina', 'Belova') #Alina is the object, Student is the class. 'Alina' maps to the name parameter of our function
#print(Alina.name, Alina.lname)
#Alina.greeting()

Sean = Student('Sean', 'Page')
#print(Sean.name, Sean.lname)
# #Sean.greeting()

# Alex = Student('Alex')
# print(Alex.name)
# #Alex.greeting()

# ===============================
# Strings are CLASSES
# ===============================
# myName = 'john'
# #that is a shortcut for:
# myName = str('john') #str is a class inside of the Python library'
# capName = myName.capitalize()

# print(capName)

# =================================
# Animal class
# =================================

# class Animal:
#     def __init__ (self, name):
#         self.name = name #uses self so all objects can be distinguished

# dog = Animal('dog')
# cat = Animal('cat')
# horse = Animal('horse')

# print(dog.name)
# print(cat.name)
# print(horse.name)

# ==============================================================
#                 Datetime Class Example
# ==============================================================
import datetime

class Person:
    def __init__(self, fname, lname, birthdate, address, email):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.address = address
        self.email = email
    
    def age(self):
        today = datetime.date.today() #gives us today's date
        age = today.year - self.birthdate.year #
        # age = age / 365
        # age = int(age) #rounds 
        # return age

        #OR

        #this compares todays date to this year + the month of the birthday + the day of the birthday
        #in this case it compares 1/21/2020, to 8/21/2020. So, we need to subtract 1 or else we will get
        #an age of 22, when in fact he is 21 and has not turned 22 yet.
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

sammy = Person('Sammy', 'Kry', datetime.date(1998, 8, 21), '123 Sesame Street', 'sammy@gmail.com')

print(sammy.fname)
print(sammy.lname)
print(sammy.birthdate)
#print(type(sammy.birthdate))
age = sammy.age()

print(age)