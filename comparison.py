# age = 25
# if (age == 25):
#     print(age)
# print(age)

#name = input("Enter in your name: ")

# if (name == 'John'):
#     print(name)

# age = 27
# if (age <= 25):
#     print(age)
# if age != 25:
#     print("You are not 25")
# if age > 25:
#     print('you are over 25')

#print(age)

#age = 26
# if age >= 21:
#   print("You get free beer")
# else:
#   print("Sorry no beer for you")


# if age >= 21:
#   print("You get free beer")
# elif age < 18:
#   print("What are you even doing here?")
# else:
#   print("Sorry no beer for you")


name_of_user = input("What is your name?: ")
length_of_name = len(name_of_user)
if length_of_name > 0 and length_of_name <= 1:
    name_of_friend = input("What is your friend's name?: ")
    greeting = f"Hello {name_of_user}, it is very nice to meet you and your friend {name_of_friend}!"
    print(greeting)
elif length_of_name > 10:
    print("Wow! You have a really long name!")
    name_of_friend = input("What is your friend's name?: ")
    greeting = f"Hello {name_of_user}, it is very nice to meet you and your friend {name_of_friend}!"
    print(greeting)
else:
    print("OK, I'll ask again some other time.")


