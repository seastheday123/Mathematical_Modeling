#Alexa Nemeth
#10/23/18
#Lesson 13:Integration

import numpy as np

#assign variables
a = 0
b = 1
N = [2,4,8,16,32,64,128]

#create sumation for the left endpoint rule
def Il(N):
    I=0
    h = (b-a)/N
    x = np.linspace(a,b, N+1)
    for i in range(1,N+1):
        I = I + (4*(x[i-1]**3) + x[i-1]**2 - 1) *h
    return I
#print values of the left endpoint rule
print("Left end-point:")
for k in N:
    print("N = {}, I = {}".format(k,Il(k)))

#create sumation for the mid point rule
def Im(N):
    I=0
    h = (b-a)/N
    x = np.linspace(a,b, N+1)
    for i in range(1,N+1):
        I = I + (4*((x[i-1] + (h/2))**3) + (x[i-1] + (h/2))**2 - 1)*h
    return I
#print values for the mid point rule
print("Mid-point:")
for k in N:
    print("N = {}, I = {}".format(k, Im(k),))