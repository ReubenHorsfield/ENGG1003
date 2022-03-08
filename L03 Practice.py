import numpy as np

x = np.array([1, 4, 9, 16, 25])
print(x)
print(x[4])
print(len(x))

t = np.array([0, 0.001, 0.002, 0.003, ...])
print(t)

t = np.linspace(0, 1, num=1001)
print(t)


import numpy as np

v0 = 5
g = 9.81
t = np.linspace(0, 1, num=1001)

y = v0*t - 0.5*g*t**2
print(y)

import matplotlib. pyplot as plt
v0 = 5
g = 9.81
t = np.linspace(0, 1, num=1001)

y = v0*t - 0.5*g*t**2
plt.plot(t, y,  'b.')
plt.xlabel('t (s)')
plt.ylabel('y (m)')
plt.title('this is a great title haha haha')
plt.grid('on')
plt.legend(['v0*t - 0.5*g*t**2'])
plt.show()



