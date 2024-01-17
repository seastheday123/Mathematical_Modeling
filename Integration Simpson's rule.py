#Alexa Nemeth
#10/23/18
#Lesson 13:Integration

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si

#assign variables
a = 0
b = 3
N = 1000
x = np.linspace(a,b, N+1) 

#create summation for Simpson's rule
def Is(N):
    i1 = 0
    i2 = 0
    h = (b-a)/N
    x1 = np.linspace(a,b, N+1)
    for i in range(1,N):
        i1 = i1 + np.exp(-(x1[i])**2)
    for k in range(1,N+1):
        i2 = i2 + np.exp(-(x1[k] - (h/2))**2)
    I = (2/np.sqrt(np.pi))*(h/6)*(np.exp(-(x1[0])**2) + np.exp(-(x1[-1])**2) + 2*i1 + 4*i2)
    return I

#define a function to take integral of
def f(x):
    return np.exp(-x**2)
#take integral of function so it can be graphed
def F(x):
    I = np.zeros(len(x))
    for i,val in enumerate(x): #set up for loop so can take integral of function up to a certian x value
        fx,err = si.quad(f,0,val) #find the intergral of the above function for a certain x value
        I[i]=fx #put value of intergral at that foint into an array
    return I

#plot the function
plt.close()
plt.plot(x,(2/np.sqrt(np.pi))*F(x),color = 'c')
plt.xlabel(r'$x$')
plt.ylabel(r'$erf(x)$')
plt.title(r'Graph of $erf(x)$ verses $x$ from 0 to 3')
plt.show()