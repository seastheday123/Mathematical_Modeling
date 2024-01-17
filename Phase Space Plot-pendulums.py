#Alexa Nemeth
#11/12/18
#Lesson 16 Homework B
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si

# define function
def F(u,t):
    return [u[1], -Om0**2*np.sin(u[0]) - 2.0*beta*u[1] \
        + gamma*Om0**2*np.cos(Om*t)]
        
    
# set initial conditions
Om = 2.0*np.pi
Om0 = 1.5*Om
beta = 0.25*Om0
gamma = 0.8
u0 = [0,0] 

#create time array
tinitial = 0.0
tfinal = 50.0
t = np.linspace(tinitial,tfinal,5001)


#solve the differential equation
u = si.odeint(F,u0,t) 
theta = u[:,0]
omega = u[:,1]

#graph the functions for t>10
plt.close()
plt.plot(theta[1000:],omega[1000:])
plt.title(r"Graph of the Phase Space for $\gamma = 0.8$")
plt.xlabel(r"$\theta$")
plt.ylabel(r"$\omega$")
plt.show()