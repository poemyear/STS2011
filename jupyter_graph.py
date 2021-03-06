import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 400.0, 0.01)
s = np.sin(np.pi * (t/180)) + np.sin(np.pi * 20 * (t/180))/7


# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
