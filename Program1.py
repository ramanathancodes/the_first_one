
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
	>>> Program1.find_type()
Enter the character:a
a is alphabet
>>> Program1.find_type()
Enter the character:3
3 is digit
>>>
>>> Program1.find_type()
Enter the character:d3
char is neither alphabet nor digit nor whitespace
>>>
>>> Program1.find_type()
Enter the character:
  is space
	"""
	char = input("Enter the character:")
	if char.isalpha():
		print(f'The enetered character {char} is alphabet')
	elif char.isdigit():
		print(f'The enetered character {char} is digit')
	elif char.isspace():
		print(f'The enetered character {char} is space')
	else:
		print("char is neither alphabet nor digit nor whitespace")


def count_type():
	"""
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




	

