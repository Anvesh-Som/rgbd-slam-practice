#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

f = open("rgbd_depth_ground_truth_correspondance.txt")
x = []
y = []
z = []
for line in f:
    if line[0] == '#':
        continue
    data = line.split()
    x.append( float(data[5] ) )
    y.append( float(data[6] ) )
    z.append( float(data[7] ) )
ax = plt.subplot( 111, projection='3d')
ax.plot(x,y,z)
plt.show()
