import cv2
import numpy as np


def mean_filter(img_, k_size):
    if len(img_.shape) == 2:
        img = img_.copy()
        img = np.expand_dims(img, -1)
    else:
        img = img_.copy()
    
    H, W, C = img.shape    
    pad = k_size // 2

    #padding
    img_pad = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)
    img_pad[pad:H+pad, pad:W+pad] = img
    
    #filtering
    out = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)
    
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[y+pad, x+pad, c] = np.mean(img_pad[y:y+k_size, x:x+k_size, c])
    
    #padding除去
    out = out[pad:H+pad, pad:W+pad]

    return out


img = cv2.imread("imori.jpg").astype(np.float32)

out = mean_filter(img, k_size=3).astype(np.uint8)

cv2.imwrite(r"out\out_11.jpg", out)
cv2.imshow("", out)
cv2.waitKey(0)
cv2.destroyAllWindows