import cv2
import numpy as np


def gaussian_filter(img_, k_size, s):
    if len(img_.shape) == 3:
        img = img_.copy()
    if len(img.shape) == 2:
        img = img_.copy()
        img = np.expand_dims(img, -1)

    H, W, C = img.shape    
    pad = k_size // 2

    #padding
    img_pad = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)
    img_pad[pad:H+pad, pad:W+pad] = img
    
    #kernel
    kernel = np.zeros((k_size, k_size))
    #kernelの中心を(x,y)=(0,0)としてガウス分布入れる
    for i in range(k_size):
        y = i - pad
        for j in range(k_size):
            x = j - pad
            kernel[i, j] = np.exp(- (x ** 2 + y ** 2) / (2 * s ** 2)) / (2 * np.pi * s ** 2)
    
    #kernelを正規化(値の合計=1にする)
    kernel /= kernel.sum()

    #filtering
    out = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)

    for y in range(pad, H+pad):
        for x in range(pad, W+pad):
            for c in range(C):
                out[y, x, c] = np.sum(img_pad[y-pad:y-pad+k_size, x-pad:x-pad+k_size, c] * kernel)
    
    #padding除去
    out = out[pad:H+pad, pad:W+pad]

    return out


img = cv2.imread("imori_noise.jpg").astype(np.float32)

out = gaussian_filter(img, k_size=3, s=1.3).astype(np.uint8)

cv2.imwrite(r"out\out_09.jpg", out)
cv2.imshow("", out)
cv2.waitKey(0)
cv2.destroyAllWindows