#Alexa Nemeth
#10/21/18
#Lesson 12:Linear Algebra
#Solution for equation:
#(2k	-k	(A1		(A1
# 			= mw^2
#-k	k)	 A2)		 A2)


import numpy as np
import matplotlib.pyplot as plt
#define variables
k = 15
m = 0.3
#create matrix with k values
M = np.matrix([[2*k, -k],[-k,k]])
#solve for eigen values and vectors
a,b = np.linalg.eig(M)

#create t-values for graphing
t = np.linspace(-5,5,1000)
print(a[1],b[0,1],b[1,1])
#graph the n1 and n2 functions for each mode
plt.close()                         
fig, (ax1) = plt.subplots(1,1)  #create one graph
ax1.plot(t,b[0,0]*np.cos(np.sqrt(a[0]/m)*t), label=r"A1") 
ax1.plot(t,b[1,0]*np.cos(np.sqrt(a[0]/m)*t), label=r"A2") 
fig, (ax2) = plt.subplots(1,1)
ax2.plot(t,b[0,1]*np.cos(np.sqrt(a[1]/m)*t), label=r"A1")
ax2.plot(t,b[1,1]*np.cos(np.sqrt(a[1]/m)*t), label=r"A2") 
ax1.set_ylabel(r'$Acos(wt)$', fontsize=16) #set the y label of the graph
ax1.set_xlabel(r"t", fontsize=16)
ax1.legend(loc = 'upper left') #show ledgend in upper left
ax2.set_ylabel(r"label", fontsize=16) #set the y label of the graph
ax2.legend(loc = 'upper left') #show ledgend in upper left
ax2.set_ylabel(r'$Acos(wt)$', fontsize=16) #set the y label of the graph
ax2.set_xlabel(r't', fontsize=16)
plt.show() 


