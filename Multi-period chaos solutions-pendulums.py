#Alexa Nemeth
#11/12/18
#Lesson 16 Homework C

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si

# define function
def F(u,t):
    return [u[1], -Om0**2*np.sin(u[0]) - 2.0*beta*u[1] \
        + gamma*Om0**2*np.cos(Om*t)]
           
#set initial conditions
Om = 2.0*np.pi
Om0 = 1.5*Om
beta = 0.25*Om0
gammavalues = [0.6, 1.073, 1.077]
u0 = [0,0]

#create time array
tinitial = 0.0
tfinal = 30.0
t = np.linspace(tinitial,tfinal,3001)

#create graphs
plt.close()
fig, ax1 = plt.subplots(1,1)
fig, ax2 = plt.subplots(1,1) 

#solve the differential equations for every gamma
for gamma in gammavalues:
    u = si.odeint(F,u0,t) 
    theta = u[:,0]
    omega = u[:,1]
    
    #plot each one for theta verse t and the phase space
    ax1.plot(t[1000:],theta[1000:], label=r"$\gamma = $"+str(gamma))
    ax2.plot(theta[1000:],omega[1000:], label=r"$\gamma = $"+str(gamma))

#create lables for graphs
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$\theta$")
ax1.legend()
ax1.set_title(r"Graph of $\theta (t)$")
ax2.set_xlabel(r"$\theta$")
ax2.set_ylabel(r"$\omega$")
ax2.legend()
ax2.set_title(r"Graph of the Phase Space with Different $\gamma$ Values")
plt.show()