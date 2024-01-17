#Alexa Nemeth
#10/23/18
#Lesson 13:Integration

import scipy.integrate as si
import matplotlib.pyplot as plt
import numpy as np

#load the data from the text file
x,y = np.loadtxt('Lesson13Data', usecols =(0,1), unpack= True)

#tak the intergral of a f(x) from the data
I =si.simps(y,x)

#print the anawer from the intergral
print("The integral of f(x) is: {}".format(I))

#graph the x and f(x) values given
plt.close()
plt.plot(x,y)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'Graph of Lesson13Data')
plt.show()