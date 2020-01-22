#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                #Blue Page #29
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#     def greet(self, other_person):
#      #print('Hello {}, I am {}!'.format(other_person.name, self.name))
#         print(f'Hello {self.name}, I am {self.name}!')

# sonny = Person('Soony', 'sonny@hotmail.com', '483-485-4948')
# jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# sonny.greet(jordan)
# jordan.greet(sonny)

# print(f'{sonny.name}\'s contact info is: {sonny.email}, {sonny.phone}')
# print(f'{jordan.name}\'s contact info is: {jordan.email}, {sonny.phone}')




#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    #Blue Page #40 - Make your own class
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print(self.year, self.make, self.model) #interestingly this does NOT print out the ,'s inside the parenthesis

# car = Vehicle('Subaru', 'Legacy', 2018)
# print(car.make, car.model, car.year)
# car.print_info()

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    #Blue Page #41 - Add a method 2
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0 #even though this is used in a later method, we must declare it here!
    
    def greet(self, other_person):
     #print('Hello {}, I am {}!'.format(other_person.name, self.name))
        print(f'Hello {self.name}, I am {self.name}!')
        self.greeting_count += 1
        print(f'Greeting count = {self.greeting_count}')
    
    def print_contact_info(self):
        print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')
   
    def add_friend(self, name):
        self.friends.append(self.name)
    
    def num_friends(self):
        return len(self.friends)
        
greeting_count = 0
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948', '')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456', '')

sonny.print_contact_info()
jordan.print_contact_info()
#sonny.friends.append(jordan)
sonny.add_friend(jordan)
#jordan.friends.append(sonny)
jordan.add_friend(sonny)

print(f'{sonny.name} has {sonny.num_friends()} friend(s)')
print(f'{jordan.name} has {jordan.num_friends()} friends(s)')

sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)


#print(f'{sonny.name} has {len(sonny.friends)} friends.')
#print(f'{jordan.name} has {len(jordan.friends)} friends.')


