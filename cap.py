import matplotlib.pyplot as plt
import numpy as np
import random
import math 
import pandas as pd
from scipy.optimize import curve_fit
tau = 0.1


# drawing theoretical graph
"""
t = np.arange(0,1,0.01)

y = 5*(1-np.e**(-t/tau))
plt.plot(t,y, label = "Capacitor Charging")
plt.axvline(x=0.1, linestyle = "--", color = "grey")
plt.axhline(y=0.63*5,linestyle = "--", color = "grey")
plt.xticks([0,0.1])
plt.yticks([0.63*5,5])
plt.xlabel("t(s)")
plt.ylabel("$V_{cap}(V)$")
plt.legend()
plt.show()
"""


"""
df = pd.read_csv("ExBCap.csv")
x = np.array(df["x"])

y = np.array(df["y"])
td = 0.1*np.log(1-y[0]/y[-1])
x = x+ td
"""

x = np.array([
    0.000,
0.100,
0.200,
0.300,
0.400,
0.500,
0.600,
0.700,
0.800,
0.900,
1.000
])
y= np.array([
    0.896,
3.299,
4.278,
4.723,
4.901,
4.990,
4.990,
4.990,
4.990,
4.990,
4.990,

])
def f(x,a,V):
    return  V*(1-np.e**(-x/a))

ydata = f(x,0.1,4.99)
popt, pcov = curve_fit(f, x, y)
print(popt
)
x_smooth = np.arange(0,1,0.01)


plt.plot(x,y, "rX",label = "Sample of the data\ncollected")

def func(x,error):
    return 4.99*(1-np.e**(-x/(0.1*(1+error))))

# drawing measured lines
plt.plot(x_smooth,f(x_smooth,popt[0],4.99),color = "black", label = f"Curve fitted line\nof data\ny={4.99}(1-e^(-t/{round(popt[0],3)}))")
plt.plot(x_smooth,func(x_smooth,0.25), "--", color = "red", label = "+25% Error in RC")
plt.plot(x_smooth,func(x_smooth,-0.25), "--", color = "navy",label = "-25% Error in RC")

# drawing area of tolerance
y_p= func(x_smooth,.25)
y_n = func(x_smooth,-.25)
plt.fill_between(x_smooth,y_p,y_n,linestyle = "--", hatch="", facecolor = "gainsboro",edgecolor="w", label = "Tolerance Range")




plt.legend()
plt.xlabel("t/s")
plt.ylabel("$V_{cap}/V$")

plt.show()
