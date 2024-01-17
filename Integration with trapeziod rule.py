#Alexa Nemeth
#10/23/18
#Lesson 13:Integration

import numpy as np

#assign values
a = 1
b = 2
N = [2,4,8,16,32,64,128,1000,10000,100000]

#create summation for the trapeziod rule
def It(N):
    I=0
    h = (b-a)/N
    x = np.linspace(a,b, N+1)
    for i in range(1,N):
        I = I + ((np.sin(x[i] + np.log(x[i])))*h)
    I = I + (h/2)*((np.sin(x[0] + np.log(x[0]))) + np.sin(x[-1] + np.log(x[-1])))
    return I

#print I values 
for k in N:
    print("I = {}".format(It(k))) 