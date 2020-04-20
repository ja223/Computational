#Question question 5
#Jagannath Das(DTP)(PhD)
import numpy as np 
import matplotlib.pyplot as plt 
a=0
b=10
N=1001 #no of iteration
x=np.linspace(a,b,N)
h=10/(len(x)-1)
# Exact solution of the given differential equation
y_exact=[0]*len(x)
for j in range(len(x)):
	y_exact[j]=-5*x[j]*(x[j]-10)
def f1(y,z,x):# Definition of dz/dx
	return -10
def f2(z):# Definition of dy/dx=z
	return z
y=np.zeros((N,)) # array of zeroes 
z=np.zeros((N,)) 
#Initial value of Y
y[0]=0
#two initial guess for z[0] ,the initial value of z will be between A and B
A=80 
B=30
#initial arbitrary non zero number 
key=2 
while abs(key)>0.0001:
	z[0]=(A+B)/2
	for i in range(N-1):# here Runge Kutta method is used for solution for a particular z
		k11=h*f1(y[i],z[i],x[i])
		k12=h*f2(z[i])
		k21=h*f1(y[i]+k12/2,z[i]+k11/2,x[i]+h/2)
		k22=h*f2(z[i]+k11/2)
		k31=h*f1(y[i]+k22/2,z[i]+k21/2,x[i]+h/2)
		k32=h*f2(z[i]+k21/2)
		k41=h*f1(y[i]+k32,z[i]+k31,x[i]+h)
		k42=h*f2(z[i]+k32)
		z[i+1]=z[i]+(k11+2*k21+2*k31+k41)/6
		y[i+1]=y[i]+(k12+2*k22+2*k32+k42)/6	
	
	key=y[N-1]
	if key>0:
		A=z[0]
	else:
		B=z[0]	
	plt.plot(x,y,color='b', linestyle='dashed')

plt.plot(x,y_exact,color='r', linestyle='solid')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title( r'$\frac{d^2x}{dt^2}+10=0$'  )	
plt.grid()
plt.show()	
