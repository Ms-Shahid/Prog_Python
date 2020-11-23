'''placeholders
for strings -> %s
for int -> %d
''' 
sent = '%s is %d years old'

print(sent%('Bob', 15))


#print('My Name is {} and my age is {}'.format(name,age))

num = int(input('Enter the number:'))

for i in range(0,num+1):

    if i % 2 ==0:
        print('Even Number : ', i)
    else:
        print('Odd Number :',i)
    
    
    