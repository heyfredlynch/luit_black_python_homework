# Python Guessing Game Ask the user to guess the year when \n
# Python 1.0 was released (the correct answer is 1994) with the following prompt:
# When was Python 1.0 released? << remember to add a space at the end of this prompt
# If the user answers 1994, show: Correct! and finish program. 

# THIS WAS MY FIRST TRY:
while True:
    year = input ('When was Python 1.0 released? ')
    if (year == '1994'):
        break
    print ('Correct!')

# DIDN'T WORK!

#Correct Answer:
while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break