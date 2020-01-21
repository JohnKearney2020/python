my_list = [2, 4, 5, 6, 19, 20]

my_dictionary = {'hello': 'world', 'square_of_two': '4', 'square_of_three': '9', 'square_of_four': '16', 0 : 1}

#==========================================
#print dictionary values based on their key
#==========================================
# print(my_dictionary['hello'])
# print(my_dictionary['square_of_three'])
# print(my_dictionary[0])

#print(my_dictionary.get(0))

#===========================
# replace a key
#===========================
# is_it_there = 'hello' in my_dictionary
# if ('hello' in my_dictionary) == True: #'hello' in my_dictionary) must be in () for this to work
#     print('True')

# my_dictionary['hello'] = 'replaced hello'
# print(my_dictionary)

#===========================
#retrieve all keys
#===========================
# keys = my_dictionary.keys()
# for key in keys:
#     #print(f'Key: {key}', end=' ')
#     print(f'Key: {key}')
# #OR
# # 
# # print(my_dictionary.keys())

#===========================
#retrieve all values
#===========================
# print(my_dictionary.values())

#============================================
#Items gives a list of tuples, key and value
#============================================
# items = my_dictionary.items()
# print(items)

# for key, value in my_dictionary.items():
#     print(f'{key}: {value}')


#===========================
#Deleting a dictionary value
#===========================
# del my_dictionary['hello']
# print(my_dictionary.keys())


#====================================================
#the in operator - see if a value is in a dictionary
#====================================================
# if is_it_there == True:
#     print(is_it_there)

# is_it_there = 'john' in my_dictionary
# if is_it_there == True:
#     print(is_it_there)

#====================================================
# List of Dictionaries
#====================================================

# contacts = [{#index 0
#     "first_name":"John",
#     "last_name":"Kearney",
#     "phone": {
#         "cell": "614-517-9783",
#         "office": "123-456-7890"
#     }
# },{#index 1
#     "first_name":"Mary",
#     "last_name":"Sue"
# },{#index 2
#     "first_name":"Brittany",
#     "last_name":"Stuart"
# }]

# #print(contacts[0])
# # print(contacts[1])
# # print(contacts[2])
# print(contacts[0]["first_name"]) #John
# print(contacts[0]["first_name"], contacts[0]["last_name"]) #John Kearney
# print(contacts[0]["first_name"], contacts[0]["last_name"], contacts[0]["phone"]["cell"] ) #John Kearney 614-517-9783

# contact = [
#     {
#         'first_name': 'Phillip',
#         'last_name': 'Guo',
#         'email': 'phillip.guo@gmail.com',
#         'phone':{
#             'work':'837-494-3948',
#             'cell': '234-897-4933'
#         }
#     },
#     {
#         'first_name': 'Mark',
#         'last_name': 'Guzdial',
#         'email': 'mark.guzdial@gatech.edu',
#         'phone':{
#             'work':'484-569-3466',
#             'cell': '493-485-9845'
#         }
#     }
# ]

# print(contact[0]['phone']['work'])


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                                    Pickle
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#====================================
#Save a dictionary to a pickle file
#====================================

# contacts = [{#index 0
#     "first_name":"John",
#     "last_name":"Kearney",
#     "phone": {
#         "cell": "614-517-9783",
#         "office": "123-456-7890"
#     }
# },{#index 1
#     "first_name":"Mary",
#     "last_name":"Sue"
# },{#index 2
#     "first_name":"Brittany",
#     "last_name":"Stuart"
# }]


#import pickle
# with open('contacts.pickle', 'wb') as fh:
#     pickle.dump(contacts, fh)  

#=============================================
#Open a pickle file and import its dictionary
#=============================================

# with open('contacts.pickle', 'rb') as fh:
#   contacts = pickle.load(fh)
#   print(contacts)

#================================================
#a check to see if the pickle file already exists:
#================================================
# import os.path
# if os.path.isfile('filename.txt'):
#     print ("File exist")
# else:
#     print ("File not exist")