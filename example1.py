"""Write a program in python which finds a letter in a string?

Example: String = "Example String", letter = "S" returns True.
"""
def find_in_letter():

	string_1 = "Example String"

	a='S' in string_1

	print(a)


print(find_in_letter())

""" Write a program in python to reverse a string using slicing method?
"""

string_2 = "helloworld!!"

x = string_2[::-1]

print(x) 


#Fuctions

class calculator:
	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a-b


#file operations
file = open('file1.txt','w')
file.write('this is python file1')

file.close()


file = open('file1.txt','r')
file.read(10)