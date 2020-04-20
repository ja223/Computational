import numpy as np
import matplotlib.pyplot as plt
# The ordinary differential equation
def f1(t,y,y1):#dy/dt=y1=f1(t,y,y1)
    return (y1)
def f2(t,y,y1):#dy1/dt=f2(t,y,y1)
    return ((2*t*y1-2*y+(t**3)*np.log(t))/(t**2))

a=1 #initial value of x
b=2 #final value of x
h= 0.01 # step-size
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
y = np.zeros((n+1,)) 
y1 =np.zeros((n+1,)) 
y_true=((7*t/4)+(0.5*t**3)*(np.log(t))-(3/4)*(t**3))
t[0]=1
y[0]=1
y1[0]=0
for i in range(1,n+1): # The formula for normal Euler method for ODE
    y1[i] = y1[i-1] + h * f2(t[i-1],y[i-1],y1[i-1])
    y[i]=  y[i-1]+h*f1(t[i-1],y[i-1],y1[i-1])

plt.xlabel('t')
plt.ylabel('y(t)')
plt.plot(t,y,color = 'r',label = 'Euler Method')
plt.plot(t,y_true,color = 'c',label = 'Analytcal Solution')
plt.title( "Forward Euler’s Method in a Python3, h= 0.01" )
plt.legend()
plt.grid()
plt.show()
