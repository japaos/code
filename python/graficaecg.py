import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

n=np.ones(11)
b=np.zeros(len(n))
ax1.plot(n,b)
