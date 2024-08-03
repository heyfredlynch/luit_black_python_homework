# assignment

sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
user_input = input('Enter a word in English or EXIT:')
if user_input == 'EXIT':
    print ('Bye!')
    break

if user_input in dictionary:
    print ('Translation: {dictionary[user_input]}')
    else:
        print('No match!"')
    
#my first try (of course I looked it up...I don't understand this yet)

# Trying to get it right
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    user_input = input('Enter a word in English or EXIT: ')
    if user_input == 'EXIT':
        break
    if user_input in sample_dict:
        print ('Translation:', sample_dict[user_input])
    else:
        print('No match!"')
        
print ('Bye!')

