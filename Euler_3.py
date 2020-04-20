#Question 2
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
# The ordinary differential equation
def f(x,y):
    return ((y/x)-(y/x)**2)

a=1 #initial value of x
b=2 #final value of x
h= 0.1 # step-size
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
y = np.zeros((n+1,)) 
y_true=x/(1+np.log(x))
x[0]=1
y[0]=1

for i in range(1,n+1): # The formula for normal Euler method for ODE
    y[i] = y[i-1] + h * f(x[i-1],y[i-1])

Abs_error=sum(y_true-y)#Absolute Error:
print('Total Absolute Error = ',Abs_error)
Rel_error=sum((y_true-y)/y_true)#Relative Error:
print('Total Relative Error = ',Rel_error)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.plot(x,y,color = 'r',label = 'Euler Method')
plt.plot(x,y_true,color = 'c',label = 'Analytcal Solution')
plt.title( "Forward Euler’s Method in a Python3, h= 0.1" )
plt.legend()
plt.grid()
plt.show()
