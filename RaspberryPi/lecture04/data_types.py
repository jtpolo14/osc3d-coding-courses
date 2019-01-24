# String literals
my_string = "Hello World"
print(type(my_string))

# String escape characters \'
# Example 1
# Wrong
#print('She's been to Japan twice')
# Example 2
# Correct
print('She\'s been to Japan twice.')

# Integer
my_int = 80
print(type(my_int))
# Converting string to integer
my_string_int = "80"
print(type(int(my_string_int)))
# ValueError | Error converting non-integer string
print(type(int(my_string)))

# Float
# value containing a decimal point
my_float = 10.0
print(type(my_float))


# Boolean
# Value that is True or False
my_true = True
print(type(my_true))
my_false = False
print(type(my_false))





