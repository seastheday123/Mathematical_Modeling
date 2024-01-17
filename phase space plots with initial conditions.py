#Alexa Nemeth
#11/12/18
#Lesson 16 Homework E

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si

#define two functions for each value of gamma
def F(u,t):
    return [u[1], -Om0**2*np.sin(u[0]) - 2.0*beta*u[1] \
        + gamma*Om0**2*np.cos(Om*t)]
def F2(u,t):
    return [u[1], -Om0**2*np.sin(u[0]) - 2.0*beta*u[1] \
        + gamma2*Om0**2*np.cos(Om*t)]
        
    
#set initial conditions
Om = 2.0*np.pi
Om0 = 1.5*Om
beta = 0.25*Om0
gamma = 1.2
gamma2 = 0.8
u0 = [0.5,0] 
u20 = [0.4999,0] 

#create time array
tinitial = 0.0
tfinal = 15.0
t = np.linspace(tinitial,tfinal,1001)


#solve the differential equation for different values of gamma and different initial conditions
u = si.odeint(F,u0,t) 
theta = u[:,0]
omega = u[:,1]
u2 = si.odeint(F,u20,t)
theta2 = u2[:,0]
omega2 = u2[:,1]

y = si.odeint(F2,u0,t) 
thetay = y[:,0]
omegay = y[:,1]
uy2 = si.odeint(F2,u20,t)
thetay2 = uy2[:,0]
omegay2 = uy2[:,1]

#find the log|theta| for each theta found
log1 = np.log10(abs(theta))
log2 = np.log10(abs(theta2))

logy1 = np.log10(abs(thetay))
logy2 = np.log10(abs(thetay2))

#graph t verse log|theta| for each case
plt.close()
fig, ax1 = plt.subplots(1,1)
fig, ax2 = plt.subplots(1,1)
ax1.plot(t,log1, label=r"$\theta(0) = $"+str(u0[0]))
ax1.plot(t,log2, label=r"$\theta(0) = $"+str(u20[0]))
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$log|\theta|$")
ax1.legend()
ax1.set_title(r"Graph of $\theta (t)$ when $\gamma = 1.2$ (chaotic)")

ax2.plot(t,logy1, label=r"$\theta(0) = $"+str(u0[0]))
ax2.plot(t,logy2, label=r"$\theta(0) = $"+str(u20[0]))
ax2.set_xlabel(r"$t$")
ax2.set_ylabel(r"$log|\theta|$")
ax2.legend()
ax2.set_title(r"Graph of $\theta (t)$ when $\gamma = 0.8$ (not chaotic)")
plt.show()