import cv2
import numpy as np


def BGR2gray(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return gray


#ndarray[条件式]で、条件を満たす要素のみを抽出
#多次元配列でも、返されるのは1次元配列
def gray2bin(img_gray, th=128):
    img_bin = img_gray.copy()
    img_bin[img_gray < th] = 0
    img_bin[img_gray >= th] = 255

    return img_bin


img = cv2.imread("imori.jpg").astype(np.float32)

img_gray = BGR2gray(img)

img_bin = gray2bin(img_gray)
img_bin = img_bin.astype("uint8")

cv2.imwrite(r"out\out_03.jpg", img_bin)
cv2.imshow("", img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()