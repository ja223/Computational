#Question question 7
#Jagannath Das(DTP)(PhD)
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt
#The Differential Equations given the questions 
def f1(t,y):
	return(t*np.exp(3*t)-2*y)
def f2(t,y):
	return(1-(t-y)**2)
def f3(t,y):
	return(1+y/t)
def f4(t,y):
	return(np.cos(2*t)+np.sin(3*t))
#The exact Solutions from mathematica are given below
def y_exact1(t):
	return((5*t-1)*np.exp(3*t)/25+np.exp(-2*t)/25)
def y_exact2(t):
	return((1-3*t+t**2)/(-3+t))
def y_exact3(t):
	return(t*2+t*np.log(t))
def y_exact4(t):
	return(np.sin(2*t)/2-np.cos(3*t)/3+8/6)
#Solution of first equation by scipy
a1=0
b1=1
y1_0=0
y_sol_1=y_exact1
sol_1=solve_ivp(f1,[a1, b1], [y1_0],t_eval=np.linspace(a1,b1))
t=np.linspace(a1,b1)
plt.plot(sol_1.t,sol_1.y[0],'r',t,y_sol_1(t),'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(0.2, 2, r"$\dot{y}=te^{3t}-2y$", fontsize=14)
plt.grid()
plt.show()
#Solution of second equation by scipy
a2=2
b2=3
y2_0=1
y_sol_2=y_exact2
sol_2=solve_ivp(f2,[a2, b2], [y2_0],t_eval=np.linspace(a2,b2))
t=np.linspace(a2,b2)
plt.plot(sol_2.t,sol_2.y[0],'r',t,y_sol_2(t),'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(2,-20, r"$\dot{y}=1-(t-y)^2$", fontsize=14)
plt.grid()
plt.show()
#Solution of Third equation by scipy
a3=1
b3=2
y3_0=2
y_sol_3=y_exact3
sol_3=solve_ivp(f3,[a3, b3], [y3_0],t_eval=np.linspace(a3,b3))
t=np.linspace(a3,b3)
plt.plot(sol_3.t,sol_3.y[0],'r',t,y_sol_3(t),'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(1,4.5, r"$\dot{y}=1+y/t$", fontsize=14)
plt.grid()
plt.show()
#Solution of Fourth equation by scipy
a4=0
b4=1
y4_0=1
y_sol_4=y_exact4
sol_4=solve_ivp(f4,[a4, b4], [y4_0],t_eval=np.linspace(a4,b4))
t=np.linspace(a4,b4)
plt.plot(sol_4.t,sol_4.y[0],'r',t,y_sol_4(t),'c')
plt.xlabel('t')
plt.ylabel('y')
plt.legend(['Solution From solve_ivp','Solution From Mathematica'])
plt.text(0.6, 1.6, r"$\dot{y}=\cos2t+\sin3t$", fontsize=16)
plt.grid()
plt.show()

