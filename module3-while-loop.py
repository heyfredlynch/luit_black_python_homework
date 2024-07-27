counter = 1
while counter < 11:
    print (counter)
    counter += 1
print ('Finished!')

# modifying the (lesser than < to a greater than) causes the loop to finish immediately.
counter = 1
while counter > 11:
    print (counter)
    counter += 1
print ('Finished!')

# remember to avoid infinate loops! That's when a loop never ends!
# incrementation is using the (counter +=1) move which is an incremental advance (by one increment)

secret_number = 14
user_input = int(input ('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print ('Wrong!')
    user_input = int(input ('Try to guess the secret number from 0 to 20: '))
print ('Perfect! You have guessed the secret number.') 


secret_number = 14
print ("""
=========================================
=========  SECRET NUMBER GAME ===========
=========================================
""")
user_input = int(input ('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print ('Wrong!')
    user_input = int(input ('Try to guess the secret number from 0 to 20: '))
print ('Perfect! You have guessed the secret number.') 