import math, random

#fucntion to generate  OTP

def generateOTP():

	#Declare a digits variable to store digits

	digits = '0123456789'

	OTP = ''

	#Length of OTP can be changed

	for i in range(4):

		OTP += digits[math.floor(random.random() * 10)]

	return OTP


# Driver code

if __name__ == '__main__':

	print('Your 4 digit OTP is: ', generateOTP())
