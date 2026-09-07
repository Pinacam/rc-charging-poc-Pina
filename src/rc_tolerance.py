import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0
VIH = 0.7 * V0

R_nominal = 10e3
C_nominal = 220e-9

R_tolerance = 0.01
C_tolerance = 0.10

# Fastest case: lowest R and lowest C
R_fast = R_nominal * (1 - R_tolerance)
C_fast = C_nominal * (1 - C_tolerance)

# Slowest case: highest R and highest C
R_slow = R_nominal * (1 + R_tolerance)
C_slow = C_nominal * (1 + C_tolerance)


def charging(t, R, C):
    return V0 * (1 - np.exp(-t / (R * C)))


def release_time(R, C):
    return -R * C * np.log(1 - VIH / V0)


t_nominal = release_time(R_nominal, C_nominal)
t_fast = release_time(R_fast, C_fast)
t_slow = release_time(R_slow, C_slow)

print("Nominal release time:", t_nominal * 1000, "ms")
print("Fastest release time:", t_fast * 1000, "ms")
print("Slowest release time:", t_slow * 1000, "ms")

t = np.linspace(0, 5 * R_slow * C_slow, 500)

fig, ax = plt.subplots()

ax.plot(
    t,
    charging(t, R_nominal, C_nominal),
    color="black",
    linewidth=2,
    label="Nominal"
)

ax.plot(
    t,
    charging(t, R_fast, C_fast),
    color="black",
    linestyle="--",
    label="Fastest"
)

ax.plot(
    t,
    charging(t, R_slow, C_slow),
    color="black",
    linestyle="-.",
    label="Slowest"
)

ax.axhline(
    VIH,
    color="0.4",
    linestyle=":"
)

ax.grid(False)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title("RC charging with component tolerance")
ax.legend()

fig.savefig("figures/generated/rc_tolerance.pdf")