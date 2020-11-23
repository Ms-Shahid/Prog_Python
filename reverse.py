
#def a num

num = int(input("Enter the number to be reversed : "))
result = 0

while(num > 0):
    
    remanider = num % 10        #12344568 % 10 = 8
    result = (result * 10) + remanider  
    num = num //10

print('The reverse of the entered number is: ' + str(result))


