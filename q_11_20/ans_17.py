import cv2
import numpy as np


def BGR2gray(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return gray


def laplacian_filter(img_, k_size=3):
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

    #kernel
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]).astype(np.float32)

    #filtering
    out = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)

    for y in range(H):
        for x in range(W):
            for c in range(C):
                region = img_pad[y:y+k_size, x:x+k_size, c]
                out[y+pad, x+pad, c] = np.sum(region * kernel)

    #padding除去
    out = out[pad:H+pad, pad:W+pad]

    #下限上限
    out = np.clip(out, 0, 255)

    return out


img = cv2.imread("imori.jpg").astype(np.float32)

img_gray = BGR2gray(img)

out = laplacian_filter(img_gray).astype(np.uint8)

cv2.imwrite(r"out/out_17.jpg", out)
cv2.imshow("", out)
cv2.waitKey(0)
cv2.destroyAllWindows