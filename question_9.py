#Question 9
#Jagannath Das(DTP)(PhD)
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def f(y,t):#Definition of the function given in the question
    return (y**2+y)/t
def rk4(w,x,h):# Definition of the Runge Kutta method
    k1 = h*f(w,x)
    k2 = h*f(w+k1/2,x+h/2)
    k3 = h*f(w+k2/2,x+h/2)
    k4 = h*f(w+k3,x+h)
    return  w+(k1+2*k2+2*k3+k4)/6
h=0.1 #step-size
N=100 # iteration
x_0=1 # initial value  of x
w1_0=-2 #initial value of y
w2_0=-2
x,w1,w2=[],[],[]
x.append(x_0)
w1.append(w1_0)
w2.append(w2_0)
Accuracy=1e-4
for i in range(N):
	W1=w1[i];W2=w2[i];X=x[i]
	if(X>=3):
		break
	y1=rk4(W1,X,h)
	y2=rk4(W2,X,2*h)
	error=abs((y1-y2)/30)
	h1=h*(Accuracy*h/error)**(1/4) # updated step-size
	if(error>Accuracy):
		h=h1
		y1=rk4(W1,X,h)
		y2=rk4(W2,X,2*h)
		w1.append(y1)
		w2=w1
	else:
		w1.append(y1)
		w2=w1
	x.append(X+h)
plt.plot(x,w1,'c',label = 'Adaptive Step Size')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
