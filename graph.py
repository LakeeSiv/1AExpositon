import matplotlib.pyplot as plt
import numpy as np

x = [
3.31E-04,
2.60E-04,
1.43E-04
]

y = np.array([
0.75767946,
0.813926571,
0.872176116,
])

avy = np.average(y)

# plt.plot(np.polyfit(x,y,1))
plt.plot(x,y, marker = "o", label = "Measured Data")
plt.plot(x,[avy,avy,avy], "--", label = f"Averaged Values Line\ny={avy}")
plt.plot(7.61E-05,	1.213312381,"rX", label = "Anomaly")
plt.title("Non-dimensional Flow Rate Vs Flow Rate")
plt.xlabel("$Flow Rate/ m^3 s^{-1} \tau$")
plt.ylabel("Non-dimensional Flow Rate")
plt.grid()
yt = np.linspace(0.7,1.2,11)
plt.legend()

plt.yticks(yt)

plt.show()