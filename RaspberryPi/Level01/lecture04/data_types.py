# String literals
# To identify the data type, you write print(type).
my_string = "Hello World"
print(type(my_string))

# String escape characters \'
# Example 1
# Wrong
# This is wrong because you can't have three single quotes on one command line. 
# You either have to use double quotes for the entire command line or use single quotes, and when you need an apostrophe, you add a backslash, then an apostrophe. 
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
print(type(int(my_string_int)))

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





