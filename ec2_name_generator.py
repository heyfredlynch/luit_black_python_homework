import random
import string

# Ask the user for the number of EC2 instances
num_instances = int(input('Enter the number of EC2 instances: '))

# Ask user for the name of their department 
department = input("What is your department name? ")

# Generate Random letters & numbers
def generate_name(dept):
    random_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    random_digits = ''.join(random.choices(string.digits, k=4))
# Combine department name, random letters, and random digits
    return f"{random_letters}{random_digits}"

 
# Generate and print the unique names
print('\nHere are your EC2 instance names:')
# Iterate Loop (calls for the letter & number creation for each EC2)
for i in range(num_instances):
    unique_name = generate_name(department)
    print(unique_name) 
