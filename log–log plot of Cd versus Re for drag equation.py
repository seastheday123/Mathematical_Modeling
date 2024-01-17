#Alexa Nemeth
#10/16/18
#Homework 10
import numpy as np
import matplotlib.pyplot as plt

#define array for Re
R = np.logspace(-1,7, 80)
#define fuction Cd
def Cd(Re):
    C = (24/Re) + ((2.6*(Re/5.0))/(1+(Re/5.0))**(1.52)) + ((0.411*(Re/263000)**(-7.94))/(1+(Re/263000)**(-8.00))) + (Re**(0.08)/461000)
    return C

#graph the function
plt.close()                    
plt.loglog(Cd(R),R, 'r') #plot y verse t
plt.suptitle(r'Graph of $C_d$ verses $R_e$')
plt.xlabel(r'$R_e$')
plt.ylabel(r'$C_d$')
plt.show()          #show the plot   