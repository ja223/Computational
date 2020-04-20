#Question question 3
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
def f1(x,y,y1):#dy/dx=y1=f1(x,y,y1)
    return (y1)
def f2(x,y,y1):#dy1/dx=f2(x,y,y1)
    return (x*np.exp(x)-x+2*y1-y)
h=0.001 #the step size
a=0 # initial value of x
b=1 # final value of x
n=int((b-a)/h) #number of iteration
x=np.linspace(a,b,n+1)
y = np.zeros((n+1,)) 
y1 = np.zeros((n+1,)) 
x[0]=0
y[0]=0
y1[0]=0
for i in range(1,n+1): # The formula for Runge Kutta fourth order for ODE
    k11=h*f1(x[i-1],y[i-1],y1[i-1])
    k12=h*f2(x[i-1],y[i-1],y1[i-1])
    k21=h*f1(x[i-1]+h/2,y[i-1]+k11/2,y1[i-1]+k12/2)
    k22=h*f2(x[i-1]+h/2,y[i-1]+k11/2,y1[i-1]+k12/2)
    k31=h*f1(x[i-1]+h/2,y[i-1]+k21/2,y1[i-1]+k22/2)
    k32=h*f2(x[i-1]+h/2,y[i-1]+k21/2,y1[i-1]+k22/2)
    k41=h*f1(x[i-1]+h,y[i-1]+k31,y1[i-1]+k32)
    k42=h*f2(x[i-1]+h,y[i-1]+k31,y1[i-1]+k32)
    y[i] = y[i-1]+(k11+2*k21+2*k31+k41)*(1/6)
    y1[i] =y1[i-1]+(k12+2*k22+2*k32+k42)*(1/6)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.plot(x,y,color = 'r',label = 'Runge Kutta fourth order  Method')
plt.title( "Runge Kutta Fourth order Method in a Python3, h= 0.001" )
plt.text(0,0.1,r"$y''-2y'+y=xe^x-x$",fontsize=12)
plt.legend()
plt.grid()
plt.show()

