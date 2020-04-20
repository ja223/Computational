#Question question 6
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
h=1 #Step size
a=0
b=10
n=int(((b-a)/h)+1)
N=100 #Number of iterations
w=np.zeros((N+1,n), dtype=float)
y_exact=np.zeros(n, dtype=float)
t=np.linspace(0,10,n)
w[:,0]=0# first column of w is zero
w[:,n-1]=0# nth column of w is zero
#The exact solution of the differential equation 
for i in range(0,n):
    y_exact[i]=-5*t[i]*t[i]+50*t[i]
#Solving linear eqns by Jaccobi Method
for j in range(0,N):
    for i in range(1,n-1):
        w[j+1,i]=(w[j,i+1]+w[j,i-1]+10*h**2)/2 
for j in range(1,N-1):
    #Candidate solution     
      plt.plot(t,w[j],color='c', label='Candidate Solution') 
    #Numerical solution
      plt.plot(t,w[N],color='b', label='Numerical Solution')
plt.plot(t,y_exact,color='r', label='Exact solution Solution') 
plt.legend()
plt.title(r'$\frac{d^2x}{dt^2}+10=0$')
plt.xlabel('t')
plt.ylabel('x')
plt.grid()
plt.show()   

