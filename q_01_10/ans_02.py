import cv2
import numpy as np


def BGR2gray(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return gray


img = cv2.imread("imori.jpg").astype(np.float32)

img_gray = BGR2gray(img).astype("uint8")

cv2.imwrite("out_02.jpg", img_gray)
cv2.imshow("", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()