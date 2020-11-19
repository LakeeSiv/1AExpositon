
# Graph for Figure 1 in lab report 



import matplotlib.pyplot as plt
import numpy as np
import random
#Generate 5 random numbers between 10 and 30
noise = random.sample(range(10, 200), 100)
print(noise)

x = np.arange(0,10,0.1)
# noise = np.random.randint(100)
plt.subplot(1,2,1)
plt.plot(x,np.sin(x)+ 0.04*np.sqrt(noise), "r")
plt.xticks([])
plt.yticks([])
plt.title("Original Wave")



plt.subplot(1,2,2)
plt.plot(x,np.sin(x))
plt.xticks([])
plt.yticks([])
plt.title("Filtered Wave")

plt.show()
print(noise)