# friends_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 27}

# #one way to get a key value from a dictionary
# print(friends_ages['Rolf'])

# #add an element to a dictionary
# friends_ages['Bob'] = 20 #this adds Bob and sets his age to 20

# #change a key value in  a dictionary - you CANNOT have duplicate keys in a dictionary, and the order of your dictionary is kept when
# #you change a value
# friends_ages ['Rolf'] = 56
# print(friends_ages)

# friends = ( #notice that this is a dictionary stored inside of a tupple
#     {'name': 'Rolf Smith', 'age': 24}, #don't forget the commas to seperate each index
#     {'name': 'Adam Wool', 'age': 30},
#     {'name': 'Anne Pun', 'age': 27}
# )

# print(friends[0]['name'])

#alternate way to print out the name at index on that is easier to read:
# friend = friends[0]
# print(friend['name'])

# ============================================
#          Dict - turn data into dictionaries
# ============================================
# friends = [('Rolf', 24), ('Adam', 30), ('Anne', 27)]
# print(friends)
# friend_ages = dict(friends) #this will turn friends into a dictionary.
# print(friend_ages)

# +++++++++++++++++++++++++++++++++++++++++++++++
# #What would the value of this code be?
# +++++++++++++++++++++++++++++++++++++++++++++++
# my_friends = {
#         'Jose': {'last_seen': 6},
#         'Rolf': {'surname': 'Smith'},
#         'Anne': 6
#     }
# print(my_friends['Jose'])

#+++++++++++++++++++++++++++++++++++++++++++++++
#What would the output of the following code be?
# +++++++++++++++++++++++++++++++++++++++++++++++

# players = [
#         {#index 0
#             'name': 'Rolf',
#             'numbers': (13, 22, 3, 6, 9)
#         },
#         {#index 1
#             'name': 'John',
#             'numbers': (22, 3, 5, 7, 9)
#         }
#     ]
# print(players[0]['numbers']) #this will print out all of Rolf's numbers
# print(players[0]['numbers'][0]) #this will just print out #13

# ==============================================
#          Iterating over dictionaries
# ==============================================
friends_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 22}
for name in friends_ages: #important to not this will only print the keys, not the values!!
    print(name)

for age in friends_ages.values(): #this will print the values!!
    print(age)

#this will print the name (key) and the ages (values)
for name, age in friends_ages.items():
    print(f'{name} is {age} years old.')