# Assign a favorite band to the variable 'fav_band'
fav_band = 'Green Day'

# Print the character at index 6 (0-based index)
print(fav_band[6])  # Output: 'D'

# Print the substring from the start up to, but not including, index 6
print(fav_band[:6])  # Output: 'Green '

# Attempt to change the character at index 6 to 'M'
# This will raise an error because strings in Python are immutable
fav_band[6] = 'M'  # TypeError: 'str' object does not support item assignment


# A string that needs to be capitalized
text = 'please capitalize me'

# Convert all characters to uppercase using the upper() method
text_cap = text.upper()

# Print the capitalized string
print(text_cap)  # Output: 'PLEASE CAPITALIZE ME'


# Prompt the user to input a number and store it as a string
user_number = input('Please provide a number!')

# Check if the entered value is numeric
if user_number.isnumeric():
    # If the input is numeric, print a thank you message
    print("Thank you, that's a correct number!")
else:
    # If the input is not numeric, print an error message
    print('Sorry,', user_number, 'is not a number!')
