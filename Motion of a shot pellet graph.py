#Alexa Nemeth
#10/16/18
#Homework 10
import numpy as np
import matplotlib.pyplot as plt

g = 9.8 #gravity    
y0 = 0 #initial height
ti = 0.0 # initial time
tf = 21 # final time
v0 = 500.0 #initial velocity
nts = 1000 # resolution
dt = (tf - ti)/nts #dt
dt2 = dt/2 #half of dt
m = .00104 #mass of pellets

#Values for R
rho = 1.28
D = 5.59*10**-3 #diameter of pellets
mu = 1.83*10**-5

A = np.pi*(D/2)**2 #cross sectional area 

#function for Cd
def Cd(Re):
    C = (24/Re) + ((2.6*(Re/5.0))/(1+(Re/5.0))**(1.52)) + ((0.411*(Re/263000)**(-7.94))/(1+(Re/263000)**(-8.00))) + (Re**(0.08)/461000)
    return C

#function for Re
def Re(v):
    R = (rho*np.abs(v)*D)/mu
    return R
#create arrays for t,y,v
t = np.linspace(ti,tf,num=nts+1)
v = np.zeros(len(t))
y = np.zeros(len(t))
#set intial values for v and y
v[0] = v0
y[0] = 0

#use RK2 to predict the y and v values in time range
for i in range(0,nts):
    yh = y[i] + v[i]*dt2
    vh = v[i] + (-g - ((rho*A*np.abs(v[i])*Cd(Re(v[i]))*v[i])/(2*m)))*dt2  
    y[i+1] = y[i] + vh*dt
    v[i+1] = v[i] + (-g - ((rho*A*np.abs(vh)*Cd(Re(vh))*vh)/(2*m)))*dt

#find max value
ymax = np.amax(y)
#find y value closest to zero
for k in range (0,len(y)):
    if -.5 <= y[k] <= .5:
        print(v[k], t[k])#print velocity and time when it hits the ground
    else:
        pass
#print max y value  
print(ymax)

#graph the v and y values verses time
plt.close()                         
fig, (ax1) = plt.subplots(1,1)
ax1.set_title(r"Graph of $y(t)$ and $v(t)$")  
ax1.plot(t,v, label=r"$v(t)$") 
ax1.plot(t,y, label=r"$y(t)$")    
ax1.set_ylabel(r"$y(t)$ and $v(t)$", fontsize=16)
ax1.set_xlabel(r"t", fontsize=16)
ax1.legend(loc = 'upper right') #show ledgend in upper right
plt.show()          #show the plot      