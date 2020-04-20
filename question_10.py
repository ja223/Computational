#Question question 10
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
def f(x,z):#dx/dz=f(x,z) here I have put z=t/(1+t) . This variabe change change the limit of t(0<=t<=inf) to z(0<=z<=1)
    return ((1)/(z**2+(x**2)*(z-1)**2))
h=0.01 #the step size
a=0 # initial value of z
b=1 # final value of z
n=int((b-a)/h)
z=np.linspace(a,b,n+1)
x = np.zeros((n+1,)) 
z[0]=1
x[0]=-2
for i in range(1,n+1): # The formula for Runge Kutta fourth order for ODE
    k1=h*f(z[i-1],x[i-1])
    k2=h*f(z[i-1]+h/2,x[i-1]+k1/2)
    k3=h*f(z[i-1]+h/2,x[i-1]+k2/2)
    k4=h*f(z[i-1]+h,x[i-1]+k3)
    x[i] =x[i-1]+(k1+2*k2+2*k3+k4)*(1/6)
print('x(t=3.5e6)=',x[n])  # AS z=t/(1+t) for given t value(3.5e6) z is almost 1 . So the value of x at the last  of the iteration i is the required value
t=z/(1-z)# back substitution of z in terms of t
plt.xlabel('t')
plt.ylabel('x(t)')
plt.plot(t,x,color = 'r',label = 'Solution Of the given Differential Equation')
plt.text(20, -1.9, r"$\frac{dx}{dt}=\frac{1}{x^2+t^2}$", fontsize=20)
plt.legend()
plt.grid()
plt.show()

