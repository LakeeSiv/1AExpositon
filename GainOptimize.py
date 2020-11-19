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

y= np.array([
    -0.05,
-0.15,
-0.62,
-1.94,
-5.03,
-11.56,
-17.22,
-23.06,
-31.31,
-36.60

])

omega = 2*np.pi*x
# gain = (1+(omega*tau)**2)**(-0.5)
# gainDB = 20*np.log(gain)/np.log(10)






def f(x,a):
    return 20*np.log((1+(2*np.pi*x*a)**2)**(-0.5))/np.log(10)

popt, pcov = curve_fit(f, x, y)

a = popt[0]

def func(x,error):
    return 20*np.log((1+(2*np.pi*x*0.1*(1+error))**2)**(-0.5))/np.log(10)

x_smooth = np.arange(0.1,1000,.1)
# print(x_smooth)


print(popt[0])

plt.xscale("log")

y_p= func(x_smooth,.25)
y_n = func(x_smooth,-.25)
plt.fill_between(x_smooth,y_p,y_n,linestyle = "--", hatch="/", facecolor = "lightgrey",edgecolor="r", label = "Tolerance Range")




# plt.plot(x,y, "rX", label = "Measurements")
# plt.plot(x_smooth,f(x_smooth,a), label = f"Curve Fitted Line\nRC={round(-a,3)}")
# plt.plot(x_smooth,func(x_smooth,.25), "--",color = "red",  label = f"+25% Error")
# plt.plot(x_smooth,func(x_smooth,-.25), "--", color = "navy", label = f"-25% Error")




plt.xlabel("f/Hz")
plt.ylabel("Gain/dB")
plt.legend()


plt.show()
