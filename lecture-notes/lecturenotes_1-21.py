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
# import datetime

# class Person:
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname
#         self.lname = lname
#         self.birthdate = birthdate
#         self.address = address
#         self.email = email
    
#     def age(self):
#         today = datetime.date.today() #gives us today's date
#         age = today.year - self.birthdate.year #
#         #this compares todays date to this year + the month of the birthday + the day of the birthday
#         #in this case it compares 1/21/2020, to 8/21/2020. So, we need to subtract 1 or else we will get
#         #an age of 22, when in fact he is 21 and has not turned 22 yet.
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1
#         return age

# sammy = Person('Sammy', 'Kry', datetime.date(1998, 8, 21), '123 Sesame Street', 'sammy@gmail.com')

# print(sammy.fname)
# print(sammy.lname)
# print(sammy.birthdate)
# #print(type(sammy.birthdate))
# age = sammy.age()

# print(age)


#======================================
#            Function Example
#======================================

# count = 0
# def greeting(name):
#     print(f'Hello {name}')
#     count += 1 #functions cannot keep a state, but classes can!
#     print(count)

# greeting('Daniela')
# greeting('Alex')
# greeting('John')
# greeting('Meryem')

#================================================================
#        Same function, but as a class that can keep a state!
#================================================================
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.count = 0
#     def greeting(self):
#         print(f'Hello, {self.name}')
#         self.count += 1
#     def printCount(self):
#         print(self.count)

# Alina = Person('Alina') #create our object
# Alina.greeting()
# Alina.printCount()
# Alina.greeting()
# Alina.printCount()
# Alina.greeting()
# Alina.printCount()

#===============================================
            #In class assignment
#===============================================  
# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#     def greet(self, other_person):
#         print(f'Hello {other_person.name}, I am {self.name}!')

# sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
# #print(sonny.name, sonny.email, sonny.phone)

# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# #print(jordan.name)
# sonny.greet(jordan)
# jordan.greet(sonny)

# print(sonny.name, sonny.email)
# print(jordan.name, jordan.email)

#------------------------------------------------------------
#Access Modifiers
#------------------------------------------------------------

# class Person:
#     def __init__ (self, name):
#         self.name = name
#         self.count = 0
#     def greet (self):
#         self._greet()
#     def _greet (self):
#         self.count += 1
#         if self.count > 1:
#             print("Stop being so nice")
#             self.__reset_count()
#         else:
#             print("Hello", self.name)
#     def __reset_count(self):
#         self.count = 0

# alex = Person('alex')
# alex.greet()
# alex.greet()
# alex.greet()

#------------------------------------------------------------
#Inheritance
#------------------------------------------------------------
# class Vstring(str):
#     def reverse(self, name):
#         rstring = ''
#         for char in name:
#             rstring = char + rstring
#         return rstring

# my_string = Vstring('hello') #we create our object here
# #print(my_string.capitalize())

# reversed = my_string.reverse('hello') #here we use the reverse method
# print(reversed)



# ---------------------------------------
#     Implicit Inheritance
# ---------------------------------------
# class Parent(object):
#     def implicit(self):
#         print("PARENT implicit()")
# class Child(Parent):
#     pass

# dad = Parent()
# son = Child()
# dad.implicit()
# son.implicit()

# class Character:
#     def __init__(self, name, power, health):
#         self.name = name
#         self.power = power
#         self.health = health

# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon
#         super(Hero, self).__init__(name, power, health) #needed to initialize the Character class b/c we dont have things
#         #defined in the Hero class
# alina = Hero('pink gun', 'alina', 3, 10)

# print(alina.weapon)


# ===========================================
#             Vehicle Class
# ===========================================

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model 
#         self.year = year
#     def print_info(self, make, model, year):
#         self.make = make
#         self.model = model 
#         self.year = year
#         print(f'{make} {model} {year}')

# car = Vehicle('Subaru', 'Legacy', 2018)
# #print(car.make, car.model, car.year)
# print_info(car)



# class Student():
#     def __init__(self, firstName, lastName, campus):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.campus = campus
#     def printStudent(self):
#         print(f"{self.firstName} {self.lastName} campus: {self.campus}")

# class Campus(): #this manages our Students class and objects
#     def __init__(self):
#         self.students = []
#     def addStudent(self, firstName, lastName, campus):
#         temp  = Student(firstName, lastName, campus)
#         self.students.append(temp)

#     def printSomeStudent(self, index):
#         print(self.students[index])
#         return self.students[index]

#     def showCurrentStudent(self):
#         for studentObject in self.students :
#             print(f"{studentObject.firstName} {studentObject.lastName} campus: {studentObject.campus}")

# alina = Student('alina', 'bolova', 'Houston')
# kazim = Student('kazim', 'oomar', 'Houston')
# alex = Student('alex', 'bishop', 'new york')
# matt = Student('matt', 'ryan', 'chicago')
# sean = Student('sean','astin', 'detroit')

# houston = Campus()
# houston.addStudent('alina', 'bolova', 'Houston')
# houston.addStudent('kazim', 'oomar', 'Houston')
# houston.addStudent('alex', 'bishop', 'new york')
# houston.addStudent('matt', 'ryan', 'chicago')
# houston.addStudent('sean','astin', 'detroit')

# houston.showCurrentStudent()

# studentObj = houston.printSomeStudent(0)
# studentObj.printStudent()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                    #Bank Account
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class AccountHolder():
    def __init__(self, first_name, last_name, middle_name, account_type, balance, status):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.account_type = account_type
        self.balance = balance
        self.status = status
    

class Bank():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.account_holders = []
    
    def addAccountHolder(self, first_name, last_name, middle_name, account_type, balance, status): #1
        if balance >= 100:
            temp  = AccountHolder(first_name, last_name, middle_name, account_type, balance, status)
            self.account_holders.append(temp)
            return print(f'Account {account_type} was successfully created for: {first_name} {middle_name} {last_name} with a balance of ${balance}')
        else:
            return print(f'Insufficient deposit amount. Must be >= $100')
    
    def showCurrentAccountHolders(self): #2
        print(f'{self.name}, located at: {self.address}, current account holders:')
        if len(self.account_holders) == 0:
            print('\tThere are currently no account holders.')
        else:
            for accountHolderObject in self.account_holders:
                print(f"\tName: {accountHolderObject.first_name} {accountHolderObject.middle_name} {accountHolderObject.last_name}, Account Type: {accountHolderObject.account_type}, Balance: ${accountHolderObject.balance}, Status: {accountHolderObject.status}")
    
    def makeTransfer(self): #3
        print('....................')
        transfer_amount = int(input('How much would you like to transfer?: '))
        print('....................')
        account_from_fname = input('What is the FIRST name of the account holder you want to TRANSFER FROM?: ')
        account_from_lname = input('What is the LAST name of the account holder you want to TRANSFER FROM?: ')
        print('....................')
        account_to_fname = input('What is the FIRST name of the account holder you want to TRANSFER TO?: ')
        account_to_lname = input('What is the LAST name of the account holder you want to TRANSFER TO?: ')
        print('....................')
        for accountHolderObject in self.account_holders: #deal with the withdrawal first
            if (accountHolderObject.last_name == account_from_lname and accountHolderObject.first_name == account_from_fname): #when we find the withdrawal account with matching first and last name
                accountHolderObject.balance -= transfer_amount
                if (accountHolderObject.balance < 0):
                    odraft_amount = 0 - accountHolderObject.balance
                    accountHolderObject.balance -= 35
                    print('....................')
                    print(f'You have overdrafted the withdrawal account by ${odraft_amount}. You have been charged a $35 overdraft fee.')
                    print(f'Your balance on the withdrawal account including all fees is now ${accountHolderObject.balance}.')
                    print('....................')
                for accountHolderObject in self.account_holders: #now we find the transfer to account. We nest this inside our first if statement so the transfer will execute only
                    #one time
                    if accountHolderObject.last_name == account_to_lname and accountHolderObject.first_name == account_to_fname:
                        accountHolderObject.balance += transfer_amount
                        print('....................')
                        print(f'You transferred ${transfer_amount} from the account of: {account_from_fname} {account_from_lname} to the account of {account_to_fname} {account_to_lname}.')
                        print(f'The new balance is ${accountHolderObject.balance}')
                        print('....................')
                        break

    def makeWithdrawal(self): #4
        withdraw_amount = int(input('How much would you like to withdraw?: '))
        account_fname = input('What is the first name of the account holder?: ')
        account_lname = input('What is the last name of the account holder?: ')
        for accountHolderObject in self.account_holders:
            if accountHolderObject.last_name == account_lname and accountHolderObject.first_name == account_fname: #when we find the account with matching first and last name
                accountHolderObject.balance -= withdraw_amount
                if accountHolderObject.balance >= 0:
                    print('....................')
                    print(f'You withdrew ${withdraw_amount} from the account of: {account_fname} {account_lname}. The new balance is ${accountHolderObject.balance}')
                    print('....................')
                else:
                    odraft_amount = 0 - accountHolderObject.balance
                    accountHolderObject.balance -= 35
                    print('....................') 
                    print(f'You have overdrafted your account by ${odraft_amount}. You have been charged a $35 overdraft fee.')
                    print(f'Your balance including all fees is now ${accountHolderObject.balance}. Have a great day!')
                    print('....................')

def main():
    wellsfargo = Bank('Wells Fargo', '123 Sesame Street')
    #populate a few placeholder accounts
    wellsfargo.addAccountHolder('Mike', 'Kearney', 'Fred', 'Checking', 500, 'Open')
    wellsfargo.addAccountHolder('Annie', 'Kearney', 'Cline', 'Checking', 500, 'Open')
    wellsfargo.addAccountHolder('Shaquille', 'Oneill', 'Money', 'Checking', 100000000, 'Open')
    action = 0
    while action != 5:
        print('1. Create an account')
        print('2. Show all account members')
        print('3. Transfer money from one account to another')
        print('4. Make a withdrawal')
        print('5. Quit')

        action = int(input('What would you like to do?: '))
        if (action == 1): #create an account
            first_name = input('What is the first name?: ')
            middle_name = input('What is the middle name?: ')
            last_name = input('What is the last name?: ')
            account_type = input('What type of account do you want to open?: ')
            balance = int(input('How much would you like to deposit?: '))
            wellsfargo.addAccountHolder(first_name, last_name, middle_name, account_type, balance, 'New')
        
        if (action == 2): #show all account holders
            wellsfargo.showCurrentAccountHolders()

        if (action == 3): #make a transfer
            wellsfargo.makeTransfer()
        if (action == 4): #make a withdrawal
            wellsfargo.makeWithdrawal()



        if (action == 6): #quit
            break
        
        
        print(' ')
        #wellsfargo.addAccountHolder('John', 'Kearney', 'David', 'Checking', 10000000000, 'Open')
        #wellsfargo.showCurrentAccountHolders()
main()



# class Bank():
#     def __init__(self):
#         self.account_holders = []
#     def addAccountHolder(self, first_name, last_name, middle_name, account_type, balance, status):
#         temp  = AccountHolder(first_name, last_name, middle_name, account_type, balance, status)
#         self.account_holders.append(temp)
#     def showCurrentAccountHolders(self):
#         for accountHolderObject in self.account_holders :
#             print(f"{accountHolderObject.first_name} {accountHolderObject.middle_name} {accountHolderObject.last_name}, Account Type: {accountHolderObject.account_type}, Balance: ${accountHolderObject.balance}, Status: {accountHolderObject.status}")

#AccountHolder(first_name, last_name, middle_name, account_type, balance, status)
# chase = Bank()
# #self, first_name, last_name, middle_name, account_type, balance, status
# chase.addAccountHolder('John', 'Kearney', 'David', 'Checking', 100000000, 'Open')