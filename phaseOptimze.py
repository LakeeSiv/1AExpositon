import matplotlib.pyplot as plt
import numpy as np
import random
import math 
import pandas as pd
from scipy.optimize import curve_fit

x = np.array([
    0.1,
0.2,
0.5,
1,
2,
5,
10,
20,
50,
100
])

y = np.array([
    0.00,
-10.40,
-21.31,
-37.62,
-54.45,
-75.58,
-80.32,
-83.30,
-91.35,
-90.04
])

def f(x,a):
    return -np.arctan(2*np.pi*x * a)*180/np.pi

popt, pcov = curve_fit(f, x, y)
a = popt[0]

def func(x,error):
    return  -np.arctan(2*np.pi*x * 0.1*(1+error))*180/np.pi

plt.xscale("log")

x_smooth = np.arange(0.1,1000,.1)
plt.plot(x,y, "rX", label = "Measurements")


# plotting area of tolerance
y_p= func(x_smooth,.25)
y_n = func(x_smooth,-.25)
plt.fill_between(x_smooth,y_p,y_n,linestyle = "--", hatch="", facecolor = "gainsboro",edgecolor="w", label = "Tolerance Range")


# plotting lines
plt.plot(x_smooth,f(x_smooth,a),color="black", label = f"Curve Fitted Line\nRC={round(-a,3)}")
plt.plot(x_smooth,func(x_smooth,.25), "--",color = "red",  label = f"+25% Error")
plt.plot(x_smooth,func(x_smooth,-.25), "--", color = "navy", label = f"-25% Error")

plt.xlabel("f/Hz")
plt.ylabel("Phase/deg")
plt.legend()


plt.show()




print(a)
