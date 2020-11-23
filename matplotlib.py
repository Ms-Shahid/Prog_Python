# import libraries

#from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
import numpy as np


#Creating a data-usage

media = ['Instagram', 'Youtube', 'Whatsapp', 'facebook',
			'Twitter','Snapchat','Hike','Messenger']


data = [27,57,43,40,10,5,15,25]


#Creating plot

fig = plt.figure(figsize = (10,10))

plt.pie(data,labels = media)


#show the plot

plt.show()
