import cv2


img = cv2.imread("imori.jpg")

img[:, :, :] = img[:, :, (2, 1, 0)]

cv2.imwrite("out_01.jpg", img)
cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#関数として書く方がいいかも
"""
def BGR2RGB(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img
"""