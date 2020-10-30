# Data Visualization Assignment

# Problem 1
from sklearn.datasets import load_iris
import numpy as np

data = load_iris().data
labels = load_iris().target
#labels = np.reshape(labels,[labels.size,1])

from sklearn.decomposition import PCA

pca = PCA(n_components = 3)
pca_data = data#np.append(data,labels, axis = 1)
X_reduced = pca.fit_transform(pca_data)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(1)
ax = Axes3D(fig)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c = labels)
plt.show()