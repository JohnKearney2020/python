# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SMALL PROBLEMS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# =========================
# 1 - Phonebook dictionary
# =========================

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
# #print(phonebook_dict['Elizabeth'])
# print(f'Elizabeth\'s phone # is: {phonebook_dict["Elizabeth"]}') #!!!!! You must use the "" quotation marker, not '' when a string is your key in an f-string.
# #add a key
# phonebook_dict['Kareem'] = 
# print(phonebook_dict)

# =========================
# In-class Phone book App
# =========================
print('Electronic Phone Book')
print('=====================')
print('1. Look up an entry')
print('2. Set an entry')
print('3. Delete an entry')
print('4. List all entries')
print('5. Quit')

phonebook = {
    'John Kearney':'614-517-9783',
    'Mary Sue':'123-456-7890',
    'Brittany Stuart':'234-678-1000',
    'Mel Kiper':'546-743-2346',
    'Jesus Christ':'879-904-2111'
    }

user_choice = input(f'What do you want to do?: ')
while user_choice != '5':
    if user_choice == '1':
        name = input('1)Look up an entry - What is the person\'s name?: ')
        if (name in phonebook) == False:
            print(f'We couldn\'t find {name} in the phonebook.')
        else:
            #print(phonebook[name])
            print(f'{name}\'s Phone Number is: {phonebook[name]}')
    elif user_choice == '2':
        name = input('2) Set an entry - What is the person\'s name?: ')
        persons_phone_num = input(f'What is the person\'s phone number?: ')
        phonebook[name] = persons_phone_num
        #print(phonebook)
    elif user_choice == '3':
        name = input('3) Delete an entry - What is the person\'s name you want to delete?: ')
        if (name in phonebook) == False:
            print(f'We couldn\'t find {name} in the phonebook.')
        else:
            #print(phonebook[name])
            del phonebook[name]
            print(f'{name} has been deleted from the phonebook.')
    elif user_choice == '4':
        print(f'4 - List all entries - Here are all the names and phone #\'s in the phonebook: ')
        for name_in_phonebook, phone_num in phonebook.items():
            print(f'{name_in_phonebook} : {phone_num}')
    else:
        print('Invalid input. Put in a number between 1 and 5.')
    user_choice = input(f'What do you want to do?: ')