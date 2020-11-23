def factorial(n):
	result =1

	for i in range(1,n+1):
		result *= i

	return result




print('factorial of 5 is = ', factorial(5))

print('factorial of 10 is = ', factorial(10))


length = float(input('Enter the length of triangle: '))
breath = float(input('Enter the breath of triangle: '))

def TriangleArea(length, breath):
	Area = 0.5 * length * breath

	return Area


print('Area of Triangle is : ',TriangleArea(length,breath))


sentence = "students floack to the arb for a variety of outdoor activites such as batmitten, chess, football,cricket"

same_letter_count = 0 	#initialize the accumulator to zero
same_letter_count = sum([i[0] == i[-1] for i in sentence.split()])

print('same_letter_count : ',same_letter_count)

print('\n')

num = int(input('Enter the number: '))

fact = 1

if num == 0:
	print(fact) 

elif num != 0 or num >0:

	while(num !=0):
		fact = fact * num
		num -=1
elif num < 0:
	print('Enter a valid number')

print('Factorail is :' ,fact)

