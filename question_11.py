#Question question 11
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
def f1(t,u1,u2,u3):
    return (u1+2*u2-2*u3+np.exp(-t))
def f2(t,u1,u2,u3):
    return (-2*np.exp(-t)+u2+u3)
def f3(t,u1,u2,u3):
    return (np.exp(-t)+u1+2*u2)
h=0.001 #the step size
a=0 # initial value of t
b=1 # final value of t
n=int((b-a)/h)
t=np.linspace(a,b,n+1)
u1 = np.zeros((n+1,)) 
u2 = np.zeros((n+1,)) 
u3 = np.zeros((n+1,)) 
t[0]=0
u1[0]=3
u2[0]=-1
u3[0]=1
for i in range(1,n+1): # The formula for Runge Kutta fourth order for ODE
    k11=h*f1(t[i-1],u1[i-1],u2[i-1],u3[i-1])
    k12=h*f2(t[i-1],u1[i-1],u2[i-1],u3[i-1])
    k13=h*f3(t[i-1],u1[i-1],u2[i-1],u3[i-1])
    k21=h*f1(t[i-1]+h/2,u1[i-1]+k11/2,u2[i-1]+k12/2,u3[i-1]+k13/2)
    k22=h*f2(t[i-1]+h/2,u1[i-1]+k11/2,u2[i-1]+k12/2,u3[i-1]+k13/2)
    k23=h*f3(t[i-1]+h/2,u1[i-1]+k11/2,u2[i-1]+k12/2,u3[i-1]+k13/2)
    k31=h*f1(t[i-1]+h/2,u1[i-1]+k21/2,u2[i-1]+k22/2,u3[i-1]+k23/2)
    k32=h*f2(t[i-1]+h/2,u1[i-1]+k21/2,u2[i-1]+k22/2,u3[i-1]+k23/2)
    k33=h*f3(t[i-1]+h/2,u1[i-1]+k21/2,u2[i-1]+k22/2,u3[i-1]+k23/2)
    k41=h*f1(t[i-1]+h,u1[i-1]+k31,u2[i-1]+k32,u3[i-1]+k33)
    k42=h*f2(t[i-1]+h,u1[i-1]+k31,u2[i-1]+k32,u3[i-1]+k33)
    k43=h*f3(t[i-1]+h,u1[i-1]+k31,u2[i-1]+k32,u3[i-1]+k33)
    u1[i] = u1[i-1]+(k11+2*k21+2*k31+k41)*(1/6)
    u2[i] =u2[i-1]+(k12+2*k22+2*k32+k42)*(1/6)
    u3[i] =u3[i-1]+(k13+2*k23+2*k33+k43)*(1/6)
    

plot1 = plt.figure(1)
plt.plot(t,u1)
plt.xlabel('t')
plt.ylabel('u1(t)')

plot2 = plt.figure(2)
plt.plot(t,u2)
plt.xlabel('t')
plt.ylabel('u2(t)')

plot3=plt.figure(3)
plt.plot(t,u3)
plt.xlabel('t')
plt.ylabel('u3(t)')


plt.show()
