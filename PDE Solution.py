#Alexa Nemeth
#Homework 20
#12/4/18

import numpy as np 
import matplotlib.pyplot as plt 

#set variable and initial conditions
xa = -5
xb = 5
c = 50
T = 25
mu = .01
J = 100
N=5000
dx=(xb-xa)/J
dt=.025*dx/c
dth = dt/2
x = np.linspace(xa,xb,J+1)
alpha = 1000

y = np.zeros(J+1)
yp = np.zeros(J+1)
v = np.zeros(J+1)
vp = np.zeros(J+1)
yten = np.zeros(J+1)
vten = np.zeros(J+1)

A = 4
sigma = 2

y = A*np.exp(-x**2/sigma**2)
v = 0*x

plt.close()

fig, ax = plt.subplots()

#solve the differential equation and plot
for n in range(1,N+1):
    yten[1:-1] = y[1:-1] + dth*v[1:-1]
    vten[1:-1] =  v[1:-1] + dth*c**2*((y[2:]-2*y[1:-1] + y[:-2])/dx**2) + dth*alpha*((y[2:]- y[:-2])/dx)

    yp[1:-1] = y[1:-1] + dt*vten[1:-1]
    vp[1:-1] = v[1:-1] + dt*c**2*((yten[2:]-2*yten[1:-1] + yten[:-2])/dx**2) + dt*alpha*((yten[2:]- yten[:-2])/dx)
    y = np.copy(yp)
    v = np.copy(vp)
    if(n%10 ==0):
        plt.plot(x,y)
plt.title(r"""$\"{y} = c^2 y' ' $$+ \alpha y' $""")
plt.xlabel('x')
plt.ylabel('y')
plt.show()