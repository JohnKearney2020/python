# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Medium PROBLEMS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# =========================
# 1 - Letter Summary
# =========================

# def letter_histogram(word):
#     dict_of_letters_f = {}
#     for each_letter in word:
#         letter_count = 0
#         for each_letter2 in word:
#             if each_letter == each_letter2:
#                 letter_count += 1
#             dict_of_letters[each_letter] = letter_count
#     return dict_of_letters_f

# word = input("Enter a word: ")
# dict_of_letters = letter_histogram(word)
# print(dict_of_letters)

#OR
# empty_dict = {}
# #word = input("Enter a word: ")
# word = 'Banana'
# for letters in word:
#     if letters not in empty_dict: #if the letter is not already in the dictionary, we create the key and set
#         #it equal to zero
#         empty_dict[letters] = 0
#     empty_dict[letters] += 1 #here we increment by one
# print(empty_dict)   


# =========================
# 2 - Word Summary
# =========================

def word_histogram(sentence):
    dict_of_words_f = {}
    for each_word in sentence:
        word_count = 0
        for each_word2 in sentence:
            if each_word == each_word2:
                word_count += 1
            dict_of_words_f[each_word] = word_count
    return dict_of_words_f

# sentence = input("Enter a sentence: ")
# sentence = sentence.lower()
# sentence = sentence.split() #split our sentence into a list of each word woot woot!
# dict_of_words = word_histogram(sentence)
# print(dict_of_words)

#OR - we can do this similar to how we did the previous problem by using 'not in'

# sent_histogram = {}
# entered_sentence = input("Please enter a sentence... ")
# sent_to_words = entered_sentence.split()
# for repeats in sent_to_words:
#     if repeats not in sent_histogram:
#         sent_histogram[repeats] = 0
#     sent_histogram[repeats] += 1
# print(sent_histogram)




# =========================
# 3 - Sorting a histogram
# =========================
def sort_and_tally(dictionary):
    # items = dictionary.items()
    sorted_dict = {}
    for each_word, each_count in dictionary.items():
        if (each_word in sorted_dict) == True: #if we've already tallied this word, skip it.
            continue
        highest_count = each_count
        highest_word = each_word
        for each_word2, each_count2 in dictionary.items():
            if (each_word2 in sorted_dict) == True: #if we've already tallied this word, skip it.
                continue
            if each_count2 > highest_count:
                highest_count = each_count2
                highest_word = each_word2
        sorted_dict[highest_word] = highest_count
    return sorted_dict


#sentence = input("Enter a sentence: ")
sentence = 'Hey ho let\'s go to the other side hey ho hey'
sentence = sentence.lower()
sentence = sentence.split() #split our sentence into a list of each word woot woot!
dict_of_words = word_histogram(sentence) #this is my function from #2
#print(type(dict_of_words))
#print(dict_of_words.sort())
sorted_and_tally_dict = sort_and_tally(dict_of_words)
print(f'The top three words are: ')
count = 0
for each_word, each_count in sorted_and_tally_dict.items():
    count += 1
    print(f'{each_word}: {each_count}')
    if count == 3: #we only want to print the top 3 
        break



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
# phonebook_dict['Kareem'] = '938-489-1234'
# #print(phonebook_dict)

# #delete an entry
# del phonebook_dict['Alice']

# #Overwrite values
# phonebook_dict['Bob'] = '968-345-2345' #Bob is already in the phonebook, so this will update his phone #
# #one way to print each name and number ********Make sure to use .items()
# for each_name, each_number in phonebook_dict.items():
#     print(f'Name: {each_name},       Phone Number: {each_number}')

# =========================
# 2 - Nested dictionaries
# =========================

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {#index 0
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {#index 1
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print(f'Ramit\'s email address is: {ramit["email"]}') # must use ""

# interests = ramit["interests"][0]
# print(f'Ramit\'s first interest is: {interests}')

# jasmine_email = ramit["friends"][0]["email"]
# print(f'Jasmine\'s email address is: {jasmine_email}')

# jan_second_interest = ramit["friends"][1]["interests"][1]
# print(f'Jan\'s second interest is: {jan_second_interest}')

# =========================
# 3 - Friend counter
# =========================
# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {#index 0
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {#index 1
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# def countFriends(dictionary):
#     friend_counter = len(dictionary['friends']) #the value of 'friends' is a list with two indeces of stuff inside
#     dictionary['friends_count'] = friend_counter
#     return dictionary
# #print(len(ramit['friends']))
# #print(ramit['friends'])
# print(countFriends(ramit))



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LARGE PROBLEMS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ============================================
# 1 - Phone Book App / In-class Phone book App
# ============================================
# print('Electronic Phone Book')
# print('=====================')
# print('1. Look up an entry')
# print('2. Set an entry')
# print('3. Delete an entry')
# print('4. List all entries')
# print('5. Quit')

# phonebook = {
#     'John Kearney':'614-517-9783',
#     'Mary Sue':'123-456-7890',
#     'Brittany Stuart':'234-678-1000',
#     'Mel Kiper':'546-743-2346',
#     'Jesus Christ':'879-904-2111'
#     }

# user_choice = input(f'What do you want to do?: ')
# while user_choice != '5':
#     if user_choice == '1':
#         name = input('1)Look up an entry - What is the person\'s name?: ')
#         if (name in phonebook) == False:
#             print(f'We couldn\'t find {name} in the phonebook.')
#         else:
#             print(f'{name}\'s Phone Number is: {phonebook[name]}')
#     elif user_choice == '2':
#         name = input('2) Set an entry - What is the person\'s name?: ')
#         persons_phone_num = input(f'What is the person\'s phone number?: ')
#         phonebook[name] = persons_phone_num #this adds the persons name and # in the phonebook
#     elif user_choice == '3':
#         name = input('3) Delete an entry - What is the person\'s name you want to delete?: ')
#         if (name in phonebook) == False:
#             print(f'We couldn\'t find {name} in the phonebook.')
#         else:
#             del phonebook[name] #this deletes the name and # from the phonebook
#             print(f'{name} has been deleted from the phonebook.')
#     elif user_choice == '4':
#         print(f'4 - List all entries - Here are all the names and phone #\'s in the phonebook: ')
#         for name_in_phonebook, phone_num in phonebook.items():
#             print(f'{name_in_phonebook} : {phone_num}')
#     else:
#         print('Invalid input. Put in a number between 1 and 5.')
#     user_choice = input(f'What do you want to do?: ')