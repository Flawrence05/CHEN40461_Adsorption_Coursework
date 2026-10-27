
# libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Setup Variables
v = 2 # m s-1
L = 30 # m
c_0 = 0 # mol m-3
t_0 = 0 # s
t_final = 100 # s
c_rate = 2 # mol m-3 s-1
t_ss = 5 # s
dz = 0.1 # m

z = np.linspace(0,L,int(L/dz)+1)
c = np.zeros(shape=z.shape)
t = np.linspace(t_0,t_final,100)

def ODEfun(t,c):
    if t <= t_ss:
        c_feed = t*c_rate
    else:
        c_feed = t_ss*c_rate
    dc_dt = np.zeros(z.size)
    dc_dt[0] = -v*(c[0] - c_feed)/dz # gradient at feed

    for i in range(1, z.size):
        dc_dt[i] = -v*(c[1] - c[i-1])/dz
    return dc_dt

sol = solve_ivp(ODEfun,[t_0, t_final],c,method='RK45',t_eval=t)

plt.plot(z, sol.y[:, 0], label="t = 0 s")
plt.plot(z, sol.y[:, 5], label=f"t = {sol.t[5]:.1f} s")
plt.plot(z, sol.y[:, -1], label=f"t = {sol.t[-1]:.1f} s")