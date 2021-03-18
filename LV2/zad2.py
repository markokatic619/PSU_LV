import numpy as np
import matplotlib.pyplot as plt
import random
brojevi = np.zeros((100,1))
for i in range(0,100):
    a = random.randint(1,6)
    brojevi[i] = a
plt.hist(brojevi, bins = 6,rwidth=0.9,align='mid')
plt.xlim([1, 6])

plt.show()