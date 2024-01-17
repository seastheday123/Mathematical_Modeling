#Alexa Nemeth
#10/23/18
#Lesson 13:Integration

import matplotlib.pyplot as plt
import numpy as np

#assign variables 
a = 0
b = np.pi/2
N = [2,4,8,16,32,64,128]

#create summation for the left endpoint rule
def Il(N):
    I = 0
    h = (b-a)/N
    x = np.linspace(a,b,N+1)
    for i in range(1,N+1):
        I = I + np.sin(x[i-1])*h
    return I
#evaluate the error
def er(N):
    return (Il(N)-1)/1

#create arrays for the log(error) and the log(h)
loger = np.zeros(len(N))
logh = np.zeros(len(N))
p=0

#find the values for above arrays
for i in N:
    loger[p] = np.log10(abs(er(N[p])))
    logh[p] = np.log10((b-a)/N[p])
    p =p + 1

#print out I terms and the error
for k in N: 
    print("I = {}, and error = {}".format(Il(k),er(k)*100))
#print out log arrays to find m
print(loger[0],logh[0])
print(loger[1],logh[1])

#graph function
plt.close()
plt.scatter(logh,loger,color = 'c')
plt.plot(logh,loger, color = 'k')
plt.ylabel(r'$log\mid error\mid$')
plt.xlabel(r'$\log(\mathcal{h})$')
plt.title(r'Graph of $log\mid error\mid$ verses $\log(\mathcal{h})$')
plt.show()