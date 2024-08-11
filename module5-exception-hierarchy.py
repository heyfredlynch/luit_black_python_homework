import sys

useer_name = input ('What is your name?')
if user_name == '':
    print('Empty name? I cannont work with that. I am closing the program, Bye Boi!')
    sys.exit()
print('Hello,', user_name)
print('Let us get started...')