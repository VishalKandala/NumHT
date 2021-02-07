import numpy as np
import matplotlib.pyplot as plt
import math

g = 9.8 # m/s^2
T_0 = np.pi/6 # rad
w_0 = 0 # rad/s

t_final = 1*np.pi # s
dt = 0.01*np.pi # s
n = int(math.ceil(t_final/dt))

def dwdt(T):
    return (-1)*g*math.sin(T)

t = 0
T = T_0
w = w_0
T_list=[T_0]
w_list=[w_0]
# Forward Euler #
for i in range(n):
    w = w+(dt)*dwdt(T)
    T = T+(dt)*w
    T_list.append(T)
    w_list.append(w)
t_list = np.linspace(0,t_final,num=n+1)

T = T_0
w = w_0
T_rk = [T_0]
w_rk = [w_0]
# RK #
for i in range(n):
    k11 = w
    k12 = dwdt(T)
    k21 = w + (dt*k12)
    k22 = dwdt(T+(k11*dt))
    T = T + (dt/2)*(k11 + k21)
    w = w + (dt/2)*(k12 + k22)
    
    T_rk.append(T)
    w_rk.append(w)

plt.figure(1)
plt.title('Displacement of Pendulum')
plt.ylabel('$\Theta$ (rad)')
plt.xlabel('t)')
plt.plot(t_list,T_list,color='r',label='Forward Euler')
plt.plot(t_list,T_rk,color='b',label='RK')
plt.legend()
plt.savefig('pendulum_disp.png')

plt.figure(2)
plt.title('Velocity of Pendulum')
plt.ylabel('$\omega$ (rad/s)')
plt.xlabel('t(s)')
plt.plot(t_list,w_list,color='r',label='Forward Euler')
plt.plot(t_list,w_rk,color='b',label='RK')
plt.legend()
plt.savefig('pendulum_vel.png')


