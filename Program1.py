
def list_my_def(library):

	"""
	List all the Functions of given Library as Arg

	Args:
		Library(string): The Library File name without .py

	Return:
		str: A Multiline string list all your functions 
				that are callable 

	Example:
		>>>list_my_def(program1)
		The list of Functions in Program1.py are 
		   1. two_int_math
	"""
	index_num = 1
	functions_list = [name for name in dir(library) if callable(getattr(library,name))]
	print("The list of functions in {}.py are".format(library))
	for function_name in functions_list:
		print("{}.{}".format(index_num,function_name))
		index_num += 1


def two_int_math(num1,num2):

	"""
	Perform arithmetic operations on two integers.

	Args:
		num1 (int): The first integer.
		num2 (int): The second integer.

	Returns:
		str: A string containing the sum of num1 and num2.

	Example:
		>>> print(two_int_math(1, 2))
		The sum is 3
		>>> print(two_int_math(1, "hen"))
		1 is not an integer
		>>> print(two_int_math(-5, 8))
		The sum is 3
 	"""
	if not isinstance(num1,int):
		print(f'{num1}  is not integer')
		return None
	if not isinstance(num2,int):
		print(f'{num2}  is not integer')
		return None
	return f"The sum is {num1+num2}"


def grade_wording():
	"""
	Print The grade in words when grade symbol is given as input

	Args:
		Nil

	Returns:
		str: Grade in words

	Example:
		>>>Program1.grade_wording()
	"""
	grade = input("Enter The Grade (O,A,B,C,F):")
	if grade == 'O':
		print("Outstanding!")
	elif grade == 'A':
		print("Very Good!")
	elif grade == 'B':
		print("Good!")
	elif grade == 'C':
		print("Average!")
	elif grade == 'F':
		print("FAIL!")
	else:
		print("Invalid Grade entered. Enter any of  (O,A,B,C,F)")

def find_type():
	"""
	Find the type of char given as input

	Args:
		Nil

	Returns:
		str: The characted type is printed

	Example:
		>>> Program1.find_type()
		Enter the character:R
		The entered character R is alphabet and in Uppercase
		>>> Program1.find_type()
		Enter the character:c
		The entered character c is alphabet and in Lowercase
		>>> Program1.find_type()
		Enter the character:2
		The entered character 2 is digit
		>>> Program1.find_type()
		Enter the character:
		The entered character   is space
	"""
	char = input("Enter the character:")
	if char.isalpha():
		if char.isupper():
			print(f'The entered character {char} is alphabet and in Uppercase')
		elif char.islower():
			print(f'The entered character {char} is alphabet and in Lowercase')
	elif char.isdigit():
		print(f'The entered character {char} is digit')
	elif char.isspace():
		print(f'The entered character {char} is space')
	else:
		print("char is neither alphabet nor digit nor whitespace")


def count_type():
	"""
	Count each type of char given as input

	Args:
		Nil

	Returns:
		str: The characted type count is printed

	Example:
	>>> Program1.count_type()
		Enter string:RaMaNatHaN4449
		lower_count is 5 and  upper_count is 5 and digit_count is 4

		>>> Program1.count_type()
		Enter string:RaMaNatHaN
		lower_count is 5 and  upper_count is 5 and digit_count is 0
	"""
	my_string = input("Enter string:")
	lower_count = sum(1 for char in my_string if char.islower())
	upper_count = sum(1 for char in my_string if char.isupper())
	digit_count = sum(1 for char in my_string if char.isdigit())
	print(f"lower_count is {lower_count} and  upper_count is {upper_count} and digit_count is {digit_count}")

def guess_the_number():
	'''
	Guess the  number being number is always 99

	Args:
		Nil

	Returns:
		"Congratulations" is number is 99 n
		If not 99 but less , say incorrect 
		if not 99 but more , say to try lower number

	Example:
		>>>Program1.guess_the_number()
		Guess the number!:12
		The number is incorrect, Try again!
		Guess the number!:23
		The number is incorrect, Try again!
		Guess the number!:45
		The number is incorrect, Try again!
		Guess the number!:3444
		Try a lower number!
		Guess the number!:34
		The number is incorrect, Try again!
		Guess the number!:99
		Congrats, The number is correct
	'''

	while 1:
		guess = int(input("Guess the number!:"))
		if guess == 99:
			print("Congrats, The number is correct")
			break
		elif guess < 99:
			print("The number is incorrect, Try again!")
		else:
			print("Try a lower number!")



	

