import math 

"""a = int(input('Enter the value of input:'))
b = int(input('Enter the value of input:'))
c = int(input('Enter the value of input:'))
"""
def quadratic(a,b,c):
    disc = b*b - 4*a*c

    if disc>0:
        print('Roots are Real and Distinct')

        r1 = (-b+math.sqrt(disc))/2*a
        r2 = (-b-math.sqrt(disc))/2*a
        print('Root1 =' + str(r1))
        print('Root2 =' + str(r2))

    elif disc==0:

        print('Roots are equal')
        r1 =  -b /2*a
        r1 =r2
        print('Root1 = Root2' + str(r1))
    else:
        print('Roots are complex')
        real = -b/(2*a)
        img = math.sqrt(disc)/2*a

        print('Root1 = ' + str(real) + 'i' + str(img))
        print('Root2 = ' + str(real) + 'i' + str(img))

    print('-------------------------------------------')

quadratic(2,4,6)
quadratic(2,5,7)


