import cv2
import numpy as np


#n*n画素ごとに分割する or s*s個に分割する
def ave_pooling(img, n=0, s=0):
    out = img.copy()
    h, w, c = img.shape

    if n:
        gy = h // n
        gx = w // n
        for i in range(gy):
            for j in range(gx):
                for k in range(c):
                    out[n*i:n*(i+1), n*j:n*(j+1), k] = np.mean(out[n*i:n*(i+1), n*j:n*(j+1), k])
    elif s:
        dy = h // s
        dx = w // s
        for i in range(s):
            for j in range(s):
                for k in range(c):
                    out[dy*i:dy*(i+1), dx*j:dx*(j+1), k] = np.mean(out[dy*i:dy*(i+1), dx*j:dx*(j+1), k])
    
    return out


img = cv2.imread("imori.jpg").astype(np.float32)

#8*8画素ごとに分割
out1 = ave_pooling(img, n=8).astype(np.uint8)

#8*8個に分割
out2 = ave_pooling(img, s=8).astype(np.uint8)

cv2.imwrite(r"out/out_07_1.jpg", out1)
cv2.imshow("", out1)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite(r"out/out_07_2.jpg", out2)
cv2.imshow("", out2)
cv2.waitKey(0)
cv2.destroyAllWindows