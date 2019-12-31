import cv2
import numpy as np


def BGR2gray(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return gray

def otsu_bin(img_gray):
    th = -1
    max_sb = -1

    for t in range(1, 256):
        c0 = img_gray[img_gray < t]
        c1 = img_gray[img_gray >= t]

        w0 = len(c0)
        w1 = len(c1)

        m0 = sum(c0) / w0 if w0 > 0 else 0
        m1 = sum(c1) / w1 if w1 > 0 else 0

        sb = (w0 * w1 * (m0 - m1) ** 2 / (w0 + w1) ** 2)
        if sb > max_sb:
            max_sb = sb
            th = t
    
    img_bin = img_gray.copy()
    img_bin[img_gray < th] = 0
    img_bin[img_gray >= th] = 255

    return img_bin


img = cv2.imread("imori.jpg").astype(np.float32)

img_gray = BGR2gray(img)

img_otsubin = otsu_bin(img_gray)

cv2.imwrite(r"out\out_04.jpg", img_otsubin)
cv2.imshow("", img_otsubin)
cv2.waitKey(0)
cv2.destroyAllWindows()