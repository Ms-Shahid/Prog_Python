

sum = 0
num = int(input('Enter the postive integer :'))

while(num != 0):
    sum = sum + num% 10
    num = num/10

print('The sum of digits of given input ' + str(num) + 'is ' + str(sum))