import numpy as np

slope = 3
y_int = 2

y = np.zeros([10,10])
x = np.arange (0,10)
x = np.tile (x,(10,1)).transpose()
noise = np.random.randn(10,10)
y = y_int + slope * x + noise

for i in np.arange (0,10):
    lin_fit = np.polyfit((x[:,i]), y[:,i],1)
    print(lin_fit)