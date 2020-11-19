import matplotlib.pyplot as plt
import numpy as np
import random
import math 
tau = 0.1




fig = plt.figure()

plt.subplot(1,2,1)
f = np.array([0.1,0.2,0.5,1,1.5,2,5,10,20,50,100])
omega = 2*np.pi*f
gain = (1+(omega*tau)**2)**(-0.5)
gainDB = 20*np.log(gain)/np.log(10)
plt.plot((f),gainDB)
tdb = 20*(math.log(np.sqrt(2)/2, 10))
print(tdb)

plt.axhline(y=tdb, linestyle = "--", color = "gray", label = "Gain=-3dB")
plt.axvline(x=1/(0.2*np.pi), linestyle = "--", color = "peru", label = "$f=f_c=1.59Hz$")
plt.xscale("log")
plt.xlabel("f/Hz")
plt.ylabel("Gain/dB")
plt.xticks([0.1,1.59,1,10,100])
plt.title("Gain Vs Frequency")
plt.legend(loc=1)

plt.subplot(1,2,2)
phase = -np.arctan(omega * tau)*180/np.pi
plt.plot(f,phase)
plt.xscale("log")
plt.ylabel("Phase/deg")
plt.xlabel("f/Hz")
# plt.legend()
plt.title("Phase Vs Frequency")

plt.show()