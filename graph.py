import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from numpy import genfromtxt
import scipy.spatial.distance as ssd
import scipy.cluster.hierarchy as hcluster

X = genfromtxt('./similarities_new.csv', delimiter=',')

distVec = ssd.squareform(X)
linkage = hcluster.linkage(distVec)
label = ["B","X's Father","B's Father","D's Father","C's Father","A's Father","E's Father",
	"Y's Mother","A","D's Mother","C's Mother","B's Mother","E's Mother",
	"Y's Father","D","D's Sister","C's Brother","C","A's Mother","E","E's Sister"]
dendro  = hcluster.dendrogram(linkage,labels = label,orientation='left',color_threshold=6)
plt.xlabel('Degree of Dissimilarity')
yellow_patch = mpatches.Patch(color='#cccc00', label='Family 1')
purple_patch = mpatches.Patch(color='#b300b3', label='Family 3')
blue_patch = mpatches.Patch(color='#00e6e6', label='Family 3')
red_patch = mpatches.Patch(color='#ff3333', label='Family 4')
green_patch = mpatches.Patch(color='#009900', label='Family 5')
plt.legend(loc='upper left',handles=[yellow_patch,purple_patch,blue_patch,red_patch,green_patch])
plt.show()
