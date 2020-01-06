import cv2
import numpy as np


def BGR2HSV(img):
    h, w, c = img.shape
    hsv = img.copy()

    for y in range(h):
        for x in range(w):
            b, g, r = img[y, x] / 255

            Max = max(b, g, r)
            Min = min(b, g, r)

            #H
            if Min == Max:
                H = 0
            elif Min == b:
                H = 60 * (g - r) / (Max - Min) + 60
            elif Min == r:
                H = 60 * (b - g) / (Max - Min) + 180
            elif Min == g:
                H = 60 * (r - b) / (Max - Min) + 300
            
            #V
            V = Max
            #S
            S = Max - Min

            hsv[y, x] = np.array([H, S, V])
    
    return hsv

def HSV2BGR(hsv):
    h, w, c = hsv.shape
    bgr = hsv.copy()

    for y in range(h):
        for x in range(w):
            H, S, V = hsv[y, x]

            C = S
            H_ = H / 60
            X = C * (1 - abs(H_ % 2 - 1))

            i, j, k = 0, 0, 0
            if H == 0 : i, j , k = 0, 0, 0
            elif 0 <= H_ < 1 : i, j, k = C, X, 0    
            elif 1 <= H_ < 2 : i, j, K = X, C, 0    
            elif 2 <= H_ < 3 : i, j, k = 0, C, X 
            elif 3 <= H_ < 4 : i, j, k = 0, X, C
            elif 4 <= H_ < 5 : i, j, k = X, 0, C
            elif 5 <= H_ < 6 : i, j, k = C, 0, X

            r = (V - C + i) * 255
            g = (V - C + j) * 255
            b = (V - C + k) * 255

            bgr[y, x] = np.array([b, g, r])

    return bgr


img = cv2.imread("imori.jpg").astype(np.float32)

hsv = BGR2HSV(img)

hsv[:, :, 0] = (hsv[:, :, 0] + 180) % 360

out = HSV2BGR(hsv).astype(np.uint8)

cv2.imwrite(r"out/out_05.jpg", out)
cv2.imshow("", out)
cv2.waitKey(0)
cv2.destroyAllWindows()