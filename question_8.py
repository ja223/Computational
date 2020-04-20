#Question question 8
#Jagannath Das(DTP)(PhD)
from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt
#The Differential Equations given the questions 
def fun1(x, y):
	return np.vstack((y[1], -np.exp(-2*y[0])))

def bc_1(ya, yb):
	return np.array([ya[0], yb[0]-np.log(2)])
def fun2(x, y):
	return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))

def bc_2(ya, yb):
	return np.array([ya[0]-1, yb[0]-np.exp(1)])
def fun3(x, y):
	return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*np.cos(x)**(-1) ))

def bc_3(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])

def fun4(x, y):
	return np.vstack((y[1], 0.5*(1-y[1]**2-y[0]*np.sin(x))  ))

def bc_4(ya, yb):
	return np.array([ya[0]-2, yb[0]-2 ])
#Solution of first equation by scipy
a1=1
b1=2
y1_0=0
x = np.linspace(a1, b1)
y_1 = np.zeros((2, x.size))
y_1[0]=y1_0
sol_1 =solve_bvp(fun1, bc_1, x, y_1)
y = np.log(x) #solution from mathematica
plt.plot(x,sol_1.sol(x)[0],'r',x,y,'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(1, 0.5, r"$y''=-e^{-2x}$", fontsize=14)
plt.grid()
plt.show()
#Solution of second equation by scipy
a2=0
b2=np.pi/2
y2_0=1
x = np.linspace(a2, b2)
y_2 = np.zeros((2, x.size))
y_2[0]=y2_0
sol_2 =solve_bvp(fun2, bc_2, x, y_2)
y = np.exp(np.sin(x)) #solution from mathematica
plt.plot(x,sol_2.sol(x)[0],'r',x,y,'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(0, 2, r"$y''=y'\cos x-y\ln y$", fontsize=14)
plt.grid()
plt.show()
#Solution of third equation by scipy
a3=np.pi/4
b3=np.pi/3
y3_0=2**(-(1/4))
x = np.linspace(a3, b3)
y_3= np.zeros((2, x.size))
y_3[0]=y3_0
sol_3 =solve_bvp(fun3, bc_3, x, y_3)
y = np.sqrt(np.sin(x))  #solution from mathematica
plt.plot(x,sol_3.sol(x)[0],'r',x,y,'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(0.8, 0.9, r"$y''=-(2y'^3+y^2y')\sec(x)$", fontsize=14)
plt.grid()
plt.show()
#Solution of fourth equation by scipy
a4=0
b4=np.pi
y4_0=2
x = np.linspace(a4, b4)
y_4= np.zeros((2, x.size))
y_4[0]=y4_0
sol_4 =solve_bvp(fun4, bc_4, x, y_4)
y = np.sin(x)+2  #solution from mathematica
plt.plot(x,sol_4.sol(x)[0],'r',x,y,'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(0.75, 2.25, r"$y''=\frac{1}{2}-\frac{y'^2}{2}-y \ \frac{\sin(x)}{2}$", fontsize=14)
plt.grid()
plt.show()

