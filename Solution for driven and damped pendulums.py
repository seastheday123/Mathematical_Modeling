#Alexa Nemeth
#11/6/18
#Lesson 15: Chaos I

import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt

#define initial conditions
O = 2*np.pi
O0 = 1.5*O
O02 = O0**2
gamma = [1.0,1.04,1.08,1.1]
T = 2*np.pi/O #2pi/omega
beta = O0/4

#create functions for different gammas
def F1(u,t):
    u3 =  -O02*np.sin(u[1]) -2*beta*u[0] + O02*np.cos(O*t)
    return [u[1],u3]

def F2(u,t):
    u3 =  -O02*np.sin(u[1]) -2*beta*u[0] + gamma[1]*O02*np.cos(O*t)
    return [u[1],u3]

def F3(u,t):
    u3 =  -O02*np.sin(u[1]) -2*beta*u[0] + gamma[2]*O02*np.cos(O*t)
    return [u[1],u3]

def F4(u,t):
    u3 =  -O02*np.sin(u[1]) -2*beta*u[0] + gamma[3]*O02*np.cos(O*t)
    return [u[1],u3]

#create initial conditions
t = np.linspace(0.0,20,201)
u0 = [0.0, 0.0]  

#solve using the odeint
u1 = si.odeint(F1,u0,t)
theta1= u1[:,0]

u2 = si.odeint(F2,u0,t)
theta2= u2[:,0]

u3 = si.odeint(F3,u0,t)
theta3= u3[:,0]

u4 = si.odeint(F4,u0,t)
theta4= u4[:,0]


#plot the t verses theta values for different gammas
plt.close()
plt.plot(t,theta1, color = 'g', label=r'$\gamma = 1$')
plt.plot(t,theta2, color = 'r', label=r'$\gamma = 1.04$')
plt.plot(t,theta3, color = 'c', label=r'$\gamma = 1.08$')
plt.plot(t,theta4, color = 'k', label=r'$\gamma = 1.1$')
plt.legend()
plt.ylabel(r'$f(t)$')
plt.xlabel(r'$t$')
plt.title(r'Graph of different $\gamma$ values')
plt.show()