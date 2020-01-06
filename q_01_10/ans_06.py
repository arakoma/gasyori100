import cv2
import numpy as np


def decrease_color(img):
    out = img.copy()
    out = out // 64 * 64 + 32
    return out


img = cv2.imread("imori.jpg")
out = decrease_color(img)

cv2.imwrite(r"out/out_06.jpg", out)
cv2.imshow("", out)
cv2.waitKey(0)
cv2.destroyAllWindows