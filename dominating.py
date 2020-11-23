# creating a dominoes game 

"""Such that the numbers varies from 1 to 6
where if we are focusing on the first element i.e 0 then,
the rest shd be 1 to 6
"""

for left in range(7):

	for right in range(7):

		print('[' + str(left) + '|' + str(right) + ']')



#Creating combinations with respect to various options

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns'] #the 4 team 

"""There is a home_team vs away_team, 
we have to make the combination in which the teams will play against
each-other, but such that the team connot battle by itself
"""

print('------Team play starts here ------')

for home_team in teams:
	
	for away_team in teams:

		if home_team != away_team:	#the team connot play to itself

			print(home_team + ' vs ' + away_team)  

			print('---------------------------')



#Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10

for i in range(1,11):

	print(i**3)


"""Write a script that prints the multiples of 7 between 0 and 100. 
Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
Remember that 0 is also a multiple of 7.
"""
for i in range(0,101):

	if i % 7 ==0:
		print(i)
