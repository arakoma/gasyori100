import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("imori_dark.jpg").astype(np.float32)

#bgrまとめてヒストグラム
plt.hist(img.ravel(), bins=255, range=(0, 255))
plt.savefig(r"out/out_20_1.png")
plt.show()

#bgrそれぞれヒストグラム
fig = plt.figure()
ax_bgr = fig.add_subplot(2, 2, 1)
ax_bgr.hist(img.ravel(), bins=255, range=(0, 255), color='k')

ax_b = fig.add_subplot(2, 2, 2)
ax_b.hist(img[..., 0].ravel(), bins=255, range=(0, 255), color='b')

ax_g = fig.add_subplot(2, 2, 3)
ax_g.hist(img[..., 1].ravel(), bins=255, range=(0, 255), color='g')

ax_r = fig.add_subplot(2, 2, 4)
ax_r.hist(img[..., 2].ravel(), bins=255, range=(0, 255), color='r')

plt.savefig(r"out/out_20_2.png")
plt.show()