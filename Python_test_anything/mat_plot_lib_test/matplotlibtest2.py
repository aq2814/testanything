# -*- coding: utf-8 -*-
'''
Created on 2015. 3. 4.

@author: D2954_IPHONE5S
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(randn(50).cumsum(), 'k--')

plt.show()
