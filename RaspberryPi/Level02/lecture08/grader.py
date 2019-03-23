# get a grade from user
# REMEMBER: the input function 
# always returns a string
score_str = input('What is the test score? ')

# convert test_score to integer
score_int = int(score_str)

# 'if' block to decide the correct letter grade
# since 'elif' is used, only one condition
# can be true otherwise the else is run 
if score_int > 89: # if score is greater than 89, print A and end
	print(score_int, 'A')
elif score_int > 79: # if score is greater than 79, print B and end
	print(score_int, 'B')
elif score_int > 69: # if score is greater than 74, print C and end
	print(score_int, 'C')
elif score_int > 64: # if score is greater than 69, print D and end
	print(score_int, 'D')
else: # if none of the above ifs are true then print F and end
	print(score_int, 'F')