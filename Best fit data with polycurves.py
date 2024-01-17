#Alexa Nemeth
#10/30/18
#Lesson 14: Least Squares Fit

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so

#load the data from the text file
x,y= np.loadtxt('polycurvedata.txt', usecols =(0,1), unpack= True)

#define the three functions being used
def fun1(x,a,b):
    return a*x + b
def fun2(x,a,b,c):
    return a*x**2 + b*x +c
def fun3(x,a,b,c,d):
    return a*x**3 + b*x**2 +c*x +d

#create values for fitting the data
p1, er = so.curve_fit(fun1,x,y)
p2, er = so.curve_fit(fun2,x,y)
p3, er = so.curve_fit(fun3,x,y)

#create x values
x1 = np.linspace(0,10,1000)

#plot the best fit lines and data in a graph
plt.close()
plt.scatter(x,y,color = 'k')
plt.plot(x1,fun1(x1,p1[0],p1[1]), color = 'g', label=r'$ax + b$')
plt.plot(x1,fun2(x1,p2[0],p2[1],p2[2]), color = 'r', label=r'$ax^2 + bx + c$')
plt.plot(x1,fun3(x1,p3[0],p3[1],p3[2],p3[3]), color = 'c', label=r'$ax^3 + bx^2 +cx +d$')
plt.legend()
plt.ylabel(r'$f(x)$')
plt.xlabel(r'$x$')
plt.title(r'Graph of polycurvedata and best fit lines')
plt.show()