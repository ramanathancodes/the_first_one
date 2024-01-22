
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




	

