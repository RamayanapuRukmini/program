import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
Fs=input("enter sampling frequency")
f1=input("enter first frequency")
f2=input("enter second frequency")
sample=100
a=np.arange(sample)
x=np.cos(2*np.pi*f1*a/Fs)
y=np.cos(2*np.pi*f2*a/Fs)
z=x+y
plt.subplot(3,1,1)
plt.plot(a,x)
plt.subplot(3,1,2)
plt.plot(a,y)
plt.subplot(3,1,3)
plt.plot(a,z)
plt.show()

