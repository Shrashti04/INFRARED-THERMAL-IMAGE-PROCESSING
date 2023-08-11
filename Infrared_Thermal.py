# -*- coding: utf-8 -*-
"""DC23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qrEKhM-qr0GJptp0u_HvDaKjwr2T02WL
"""

import cv2 as cv
import numpy as np
import random
import math
import numpy as np
from google.colab.patches import cv2_imshow

import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

im=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/1(09).jpg')
cv2_imshow(im)

im=cv.imread(r'https://drive.google.com/file/d/1sy14ffOjYz6ZTvrpPLcFof4WQ27GNY7y/view?usp=sharing')
print(im)

for i in range(315):
    for j in range(389):
        if im[i][j][2]>100:
            im[i][j]=[255]*3
        else:
            im[i][j]=[0]*3
cv2_imshow(im)

im.shape

drop, bg = im[200][0], im[200][200]
epochs = 10000

cluster = np.zeros((315, 389))          # 0: drop, 1: bg

for iter in range(epochs):

    ndrop = nbg = 0

    for i in range(315):
        for j in range(389):
            cluster[i][j] = int(np.linalg.norm(im[i][j]-drop) < np.linalg.norm(im[i][j]-bg))
            ndrop += 1 - cluster[i][j]
            nbg += cluster[i][j]

    drop = sum([im[i][j] for i in range(315) for j in range(389)  if not(cluster[i][j])]) / (1+ndrop)
    bg = sum([im[i][j] for i in range(315) for j in range(389)  if not(cluster[i][j])]) / (1+nbg)

for i in range(315):
        for j in range(389):
            if (cluster[i][j]):
                im[i][j] = [1]*3
            else:
                im[i][j] = [255]*3
cv2_imshow(im)



"""# Sklearn clustering: pixels as RGB vectors

"""

from sklearn.cluster import KMeans
import numpy as np

im=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/1(09).jpg')
X = np.array([im[i][j] for i in range(315) for j in range(389)])
kmeans = KMeans(n_clusters=2).fit(X)

segmented_im = im.copy()
for i in range(315):
    for j in range(389):
        if not(kmeans.predict([segmented_im[i][j]])):
            segmented_im[i][j]=[0]*3
        else:
            segmented_im[i][j]=[255]*3

cv2_imshow(segmented_im)

# manually segmented: pix[2]>100

im=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/1(09).jpg')
manSegmented_im = im.copy()

for i in range(315):
    for j in range(389):
        if manSegmented_im[i][j][2]>100:
            manSegmented_im[i][j]=[255]*3
        else:
            manSegmented_im[i][j]=[0]*3

cv2_imshow(segmented_im)
cv2_imshow(im)
cv2_imshow(manSegmented_im)

im01=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(02).bmt')
cv2_imshow(im01)

im18=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(18).bmt')
cv2_imshow(im18)

im08=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(08).bmt')
cv2_imshow(im08)

"""# Clustering with outer frame
# adding coordinate as additional feature: failed
"""

im08=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(08).bmt')
M,N,_ = im08.shape
X = np.array([np.append(im08[i][j],[i,j]) for i in range(M) for j in range(N)])
kmeans = KMeans(n_clusters=3).fit(X)

segmented_im = im08.copy()
for i in range(M):
    for j in range(N):
        segmented_im[i][j] = [kmeans.predict([np.append(im08[i][j],[i,j])])[0]*127.5]*3
cv2_imshow(segmented_im)

im08=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(08).bmt')
M,N,_ = im08.shape
X = np.array([np.append(im08[i][j],[i,j]) for i in range(M) for j in range(N)])
kmeans = KMeans(n_clusters=2).fit(X)

segmented_im = im08.copy()
for i in range(M):
    for j in range(N):
        segmented_im[i][j] = [kmeans.predict([np.append(im08[i][j],[i,j])])[0]*255]*3
cv2_imshow(segmented_im)

im08=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(08).bmt')
M,N,_ = im08.shape
X = np.array([im08[i][j] for i in range(M) for j in range(N)])
kmeans = KMeans(n_clusters=3).fit(X)

segmented_im = im08.copy()
for i in range(M):
    for j in range(N):
        segmented_im[i][j] = [kmeans.predict([im08[i][j]])[0]*127.5]*3
cv2_imshow(segmented_im)

im08=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(08).bmt')
M,N,_ = im08.shape
X = np.array([im08[i][j] for i in range(M) for j in range(N)])
kmeans = KMeans(n_clusters=2).fit(X)

segmented_im = im08.copy()
for i in range(M):
    for j in range(N):
        segmented_im[i][j] = [kmeans.predict([im08[i][j]])[0]*255]*3
cv2_imshow(segmented_im)

im08=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/1(11).bmt')
cv2_imshow(im08)

ax = plt.axes(projection='3d')
M,N,_ = im08.shape

R = np.array([im08[i][j][0] for i in range(M) for j in range(N)])
G = np.array([im08[i][j][1] for i in range(M) for j in range(N)])
B = np.array([im08[i][j][2] for i in range(M) for j in range(N)])

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

color = []
for i in range(M):
    for j in range(N):
        color.append('#'+rgb_to_hex(tuple(im08[i][j])))

ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')
ax.scatter3D(R,G,B,s=0.0001,c=color)

im08=cv.imread(r'/content/drive/MyDrive/Stock images/butterfly.jpg')

ax = plt.axes(projection='3d')
M,N,_ = im08.shape

R = np.array([im08[i][j][0] for i in range(M) for j in range(N)])
G = np.array([im08[i][j][1] for i in range(M) for j in range(N)])
B = np.array([im08[i][j][2] for i in range(M) for j in range(N)])

ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')
ax.scatter3D(R,G,B,s=0.2)

imScale = cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/tempScale.png')

ax = plt.axes(projection='3d')
M,N,_ = imScale.shape
print(M,N)

R = np.array([imScale[i][12][0] for i in range(M)])
G = np.array([imScale[i][12][1] for i in range(M)])
B = np.array([imScale[i][12][2] for i in range(M)])

ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')
ax.scatter3D(R,G,B,s=0.5)

x = [0, 1, 1, 2, 2, 3]
y = [0, 1, 2, 1, 2, 3]

#color
color = [imScale[0][j] for j in range(6)]

#scatter plot
plt.scatter(x, y, c = color)

plt.show()

color

imScale = cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/tempScale.png')
cv2_imshow(imScale)

imC = cv.applyColorMap(imScale, cv.COLORMAP_JET)
cv2_imshow(imC)

imScale = cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/tempScale.png')

ax = plt.axes(projection='3d')
M,N,_ = imScale.shape

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

color = []
for i in range(M):
    color.append('#'+rgb_to_hex(tuple(imScale[i][12])))

R = np.array([imScale[i][12][0] for i in range(M)])
G = np.array([imScale[i][12][1] for i in range(M)])
B = np.array([imScale[i][12][2] for i in range(M)])

ax.set_xlabel('R')
ax.set_ylabel('G')
ax.set_zlabel('B')
ax.scatter3D(R,G,B,s=10,c=color)

imScale = cv.imread(r'/content/drive/MyDrive/thermal images- DC22/115/tempScale.png')
M,N,_ = imScale.shape

print(M,N)
cv2_imshow(imScale)
for i in range(M):
    for j in range(1):
        print(imScale[i][j])

M, N

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# a, b = 0, 1
# for i in range(10000):
#   a, b = b, a+b

import time

from sklearn.cluster import KMeans
import numpy as np

im=cv.imread(r'/content/drive/MyDrive/thermal images- DC22/1(09).jpg')
X = np.array([im[i][j] for i in range(315) for j in range(389)])
kmeans = KMeans(n_clusters=2).fit(X)

segmented_im = im.copy()
sum=0

start_time = time.perf_counter()
for i in range(315):
    for j in range(389):
        if not(kmeans.predict([segmented_im[i][j]])):
            segmented_im[i][j]=[0]*3
            sum+=1
        else:
            segmented_im[i][j]=[255]*3
end_time = time.perf_counter()

print(end_time-start_time)
cv2_imshow(segmented_im)
print(sum)

import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

# Load the image and convert it to a 2D array
image = cv.imread(r'/content/drive/MyDrive/thermal images- DC22/1(09).jpg') # Load the image using your preferred method
X = np.reshape(image, (-1, 3)) # Reshape the image into a 2D array of pixels

# Use KMeans to segment the image into 2 clusters
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Extract the cluster labels and reshape them back into the original image shape
labels = kmeans.labels_
segmented_image = np.reshape(labels, image.shape[:2])

cv2_imshow(segmented_image)