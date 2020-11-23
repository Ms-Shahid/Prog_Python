import socket 

hostname = input('Enter hostname: ')	#hostaman is the name of admin of machine ex: ms

hostname = socket.gethostname()

IpAddr = socket.gethostbyname(hostname)

# gives a ip address
print('IP Address is: ' + IpAddr)

print('**************************')
# list of Alphabets
alpha =[]

for i in range(65, 91):
	alpha.append(chr(i))

print(alpha)

