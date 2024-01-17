#Alexa Nemeth
#11/12/18
#Lesson 16 Homework D

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si

#define function
def F(u,t):
    return [u[1], -Om0**2*np.sin(u[0]) - 2.0*beta*u[1] \
        + gamma*Om0**2*np.cos(Om*t)]
    
#set initial consitions
Om = 2.0*np.pi
Om0 = 1.5*Om
beta = 0.25*Om0
gamma = 1.2
u0 = [0,0] 

#create time array
tinitial = 0.0
tfinal = 50.0
t = np.linspace(tinitial,tfinal,5001)

#solve the differential equation
u = si.odeint(F,u0,t) 
theta = u[:,0]
omega = u[:,1]

#create graphs
plt.close()
fig, ax1 = plt.subplots(1,1)
fig, ax2 = plt.subplots(1,1)
ax1.plot(t[1000:],theta[1000:])
ax2.plot(theta[1000:],omega[1000:])
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$\theta$")
ax1.set_title(r"Graph of $\theta (t)$")
ax2.set_xlabel(r"$\theta$")
ax2.set_ylabel(r"$\omega$")
ax2.set_title(r"Graph of the Phase Space for $\gamma = 1.2$")
plt.show()