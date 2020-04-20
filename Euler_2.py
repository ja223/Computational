#Question 1 second part
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
# The ordinary differential equation
def f(x,y):
    return -20*(y-x)**2+2*x

a=0 #initial value of x
b=1 #final value of x
h= 0.001 # step-size
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
y = np.zeros((n+1,)) 
x[0]=0
y[0]=(1/3)

for i in range(1,n+1): # The formula for backward Euler method for ODE
    k= y[i-1] + h * f(x[i-1],y[i-1])
    y[i] = y[i-1] + h * f(x[i],k)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title( "Backward integration with Euler’s Method in a Python, h= 0.001" )
plt.grid()
plt.show()
