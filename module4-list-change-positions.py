# Prompt the user to enter the first number and store it as a string
first = input('Enter first number: ')

# Prompt the user to enter the second number and store it as a string
second = input('Enter second number: ')

# Print the numbers before attempting to swap
print('Before swapping:', first, second)

# Attempt to swap the numbers (Note: This will not work as intended)
first = second
second = first

# Print the numbers after the incorrect swap attempt
print('After swapping:', first, second)
# This method doesn't work because both 'first' and 'second' now refer to the same value.

# Correct method to swap variables
# Prompt the user to enter the first number again
first = input('Enter first number: ')

# Prompt the user to enter the second number again
second = input('Enter second number: ')

# Print the numbers before swapping
print('Before swapping:', first, second)

# Correctly swap the values of 'first' and 'second'
first, second = second, first

# Print the numbers after swapping
print('After swapping:', first, second)

# List of top cities
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Swap the first and last cities in the list
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]

# Print the list after swapping
print(top_cities)

# Reset the list of top cities
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Sort the cities alphabetically
top_cities.sort()

# Print the sorted list
print(top_cities)

# List of random numbers
random_numbers = [2, 5, 0, -3, 4]

# Sort the numbers in ascending order
random_numbers.sort()

# Print the sorted list
print(random_numbers)

# Reset the list of random numbers
random_numbers = [2, 5, 0, -3, 4]

# Sort the numbers in descending order
random_numbers.sort(reverse=True)

# Print the sorted list
print(random_numbers)

# List of top cities
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# Use the sorted() function to get a sorted copy of the list
print(sorted(top_cities))

# Print the original list to show it has not been modified
print(top_cities)
