import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0 #supply voltage
R = 10e3 #resistance
C = 22e-12 #capacitance

tau = R * C #time constant
t=np.linspace(0, 5*tau, 500)
V = V0*(1-np.exp(-t / tau))

plt.plot(t, V, color='black')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title("Capacitor charging")
plt.show()

print("tau=", tau, "s ; V(tau)=", V0*(1-np.exp(-1)), "V")
