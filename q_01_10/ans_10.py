import cv2
import numpy as np


def median_filter(img_, k_size):
    if len(img_.shape) == 3:
        img = img_.copy()
    if len(img_.shape) == 2:
        img = img_.copy()
        img = np.expand_dims(img, -1)

    k = k_size
    H, W, C = img.shape    
    pad = k_size // 2

    #padding
    img_pad = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)
    img_pad[pad:H+pad, pad:W+pad] = img
    
    #filtering
    out = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)
    """
    if k * k % 2 == 1:
        odd= True
    else:
        odd= False
    """
    for y in range(H):
        for x in range(W):
            for c in range(C):
                """
                if odd:
                    filter = np.sort(img_pad[y:y+k, x:x+k, c].reshape(k * k))
                    med = filter[k*k//2]
                else:
                    filter = np.sort(img_pad[y:y+k, x:x+k, c].reshape(k * k))
                    idx = k * k // 2
                    med = (filter[idx] + filter[idx+1]) / 2
                out[y+pad, x+pad, c] = med
                """
                out[y+pad, x+pad, c] = np.median(img_pad[y:y+k, x:x+k, c])
    
    #padding除去
    out = out[pad:H+pad, pad:W+pad]

    return out


img = cv2.imread("imori_noise.jpg").astype(np.float32)

out = median_filter(img, k_size=3).astype(np.uint8)

cv2.imwrite(r"out\out_10.jpg", out)
cv2.imshow("", out)
cv2.waitKey(0)
cv2.destroyAllWindows