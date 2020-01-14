#print("I\'m a string")

#concatinating

#print("Hello" + " world")

#escape symbols
# print('I\'m a string')
# print('I\'m a \t\t\t\t string')
# print('I\'m a \v\v\v\v string')
#print("hello \nworld")

# name = "John"
# lname = "Kearney"

# output = "Good morning {student1} {student2}".format(student1=name,student2=lname)
# print(output)

#f strings - these are the newer standard
# student1 = "John"
# student2 = "Diego"
# output = f'hello world {student1} {student2}'
#print(output)
# print(type(student1))

# test = "5"
# print(isinstance(test, int))

# consolelog = input("Enter your name: ")
# output = f'Hello {consolelog}.'
# dataType = str(type(consolelog))

# print(output + "The data type is: " + dataType)

input_number_from_user = input("Insert a number: ")
print(type(input_number_from_user))

casted_output = int(input_number_from_user)
print(type(casted_output))

some_math = casted_output * 7
print(some_math)