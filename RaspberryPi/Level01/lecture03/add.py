# use the built-in python function 'input'
# to get a number from the user. The number
# will be stored in a variable named string_number1
string_number1 = input('Enter a number: ')

# use the built-in python function 'input'
# to get a number from the user. The number
# will be stored in a variable named string_number2
string_number2 = input('Enter a number: ')

# convert the string into an integer so the numbers can be added together
integer_answer = int(string_number1) + int(string_number2)
print(integer_answer)

# use the built-in python function print to output
# the variable integer_answer 5 times to the screen
print('The answer is', integer_answer)
