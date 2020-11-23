"""Need to prepare the report, 
to manage the users interaction with respect 
to login and logged out actions"""

"""Let us first divide the problem into steps
Step1:

1-->What info we need as input and output 
2-->We need to generate a list of Events,
	were each event is a instance of the event class
3-->The event class contains the data such as,
	*Date when the event has been occured
	*name of the event
	*user interaction
	*And event type

**The Attributies we need to know are:
1)Date
2)User
3)Machine
4)Type
5)Event Type
	*Login 
	*logged out


#Lets take a small example
numbers = [1,3,5,8,6,2]
numbers.sort()
print(numbers)

names= ['Charly','Basr','Tig','Ruby']
print('The unsorted list is:', names)

print('The sorted list is:', sorted(names))

print('Sorting w.r.t to key(len)', sorted(names, key=len))

"""

def get_event_date(event):
	return event.date

def current_users(events):
	events.sort(key=get_event_date)
	machines = {}
	for event in events:
		if event.machine not in machines:
			machines[event.machine] = set()
		if event.type == 'login':
			machines[event.machine].add(event.user)
		elif event.type == 'logout' and event.user in machines[event.machine]:
			machines[event.machine].remove(event.user)
	return machines

def generate_report(machines):
	for machine, users in machines.items():
		if len(users) > 0:
			user_list = ", ".join(users)
			print("{}: {}".format(machine,user_list))

class Event:
	def __init__(self,event_date,event_type,machine_name,user):
		self.date = event_date
		self.type = event_type
		self.machine = machine_name
		self.user = user 
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

print('generate the Report :', generate_report(users) )



"""
non_punctuation_text = ""
    for char in file_contents:
        if char not in punctuations:
            non_punctuations_text = non_punctuation_text + char
    words = non_punctuation_text.split()
    clean_words = []
    frequencies = {}
    
    for word in words:
        if word.isalpha():
            if word not in uninteresting_words:
                clean_words.append(word)
    for alpha_word in clean_words:
        if alpha_word not in frequencies:
            frequencies[alpha_word] =1
        else:
            frequencies[alpha_word] +=1
            """
