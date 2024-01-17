#Alexa Nemeth
#11/14/18
#Lesson 18: Numerical Differentiation

import numpy as np
import matplotlib.pyplot as plt

#set N,x, and h values 
N = 100
x = np.linspace(-10.0, 10.0, N+1)
h = 20.0/N

#create functions for f and f'
def f(x):
    return np.sin(x**2/5)
def fpa(x):
    return (2/5)*x*np.cos(x**2/5)

#compute numerically 
    
fp = np.zeros(len(x))
#three point centered stencil 
for i in range(0,len(x),1):
    k = x[i]-h
    j = x[i]+h
    fp[i] = (f(j)-f(k))/(2*h)
#three point one sided stencil at end points 
x0=x[0]
i = x0-h
n = x0-2*h
fp[0] = (3*f(x0) - 4*f(i) + f(n))/(2*h)

xe=x[-1]
t = xe-h
s = xe-2*h
fp[-1] = (3*f(xe) - 4*f(t) + f(s))/(2*h)   

#graph both functions 
plt.close()
fig, (ax1, ax2) = plt.subplots(2,1) 
ax2.set_title(r"Graph of $f'(x)$ of $f(x)=sin(x^2/5)$ numerically")
ax1.set_title(r"Graph of $f'(x)$ of $f(x)=sin(x^2/5)$ analytically")
ax1.set_xlabel("x")
ax1.set_ylabel("f'(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("f'(x)")
ax2.plot(x,fp,'g')
ax1.plot(x,fpa(x),'b')
plt.show()