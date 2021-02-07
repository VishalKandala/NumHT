import numpy as np
import math
import matplotlib.pyplot as plt

#constants#
h = 400 # W/m^2.K
A_s = 4e-3 # m^2
rho = 8500 # kg/m^3
V = 2.25e-5 # m^3
c = 400 # j/kg.K 
T_inf = 473.15 # K
T_0 = 303.15 # K
dt = 0.5 # s
t_f = 18 # s
n = int(math.ceil(18/0.5))
const = h*A_s/(rho*V*c)

#print(const)

# Functions#

def f(T):
    f=(-1)*((h*A_s)/(rho*V*c))*(T-T_inf)
    return f

# main #
T = T_0 
t = 0
T_list = [T]
for i in range(n):
#    print("T_init:",T)
    k1 = f(T)
#    print("k1:",k1)
    T1 = T+(dt*k1/2)
#    print("T1:",T1)
    k2 = f(T1)
#    print("k2:",k2)
    T2 = T+(dt*k2/2)
#    print("T2:",T2)
    k3 = f(T2)
#    print("k3:",k3)
    T3 = T+(dt*k3)
#    print("T3:",T3)
    k4 = f(T3)
#    print("k4:",k4)
    T = T+((dt/6)*(k1 + (2*k2) + (2*k3) + k4))
    T_list.append(T)
#    print("T_final:",T)

#print(T_list)
T_list =  np.array(T_list)
t_list = np.linspace(0,t_f,num=n+1)
T_anal = T_inf-(1/(np.exp(const*t_list-(np.log(T_inf-T_0)))))

plt.title('Lumped Capacitance Method')
plt.xlabel('t(s)')
plt.ylabel('T(K)')
plt.plot(t_list,T_list,color='r',label='RK4')
plt.plot(t_list,T_anal,color='b',label='Analytical')
plt.legend()
plt.savefig('heat.png')
