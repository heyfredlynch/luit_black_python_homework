input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

def get_average (input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print (average)

# 2nd version of the code but I'm turning this code into my function:


def get_average (input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print (average)

get_average ([5.0, 3.5, 7.8, 9.9, 10.0])

# So here, "get average" has become my 'auto funtion' and the list of numbers
# in  the brackets [5.0, 3.5, 7.8, 9.9, 10.0] are the argument. 

def get_average (input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    print (average)

get_average ([1,10])

def print_letter_count(text, letter):
    counter = 0
    for char in text: 
        if char == letter:
            counter += 1
    print ('Number of', letter, 'is', counter)


print_letter_count ('Welcome', 'e')

print_letter_count ('People say nothing is impossible, but I do nothing every day.', 'a')

print_letter_count ('e', 'Welcome')

print_letter_count (letter ='e', text='Welcome')