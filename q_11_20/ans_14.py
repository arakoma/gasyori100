import cv2
import numpy as np


def BGR2gray(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return gray


def differential_filter(img_, k_size=3):
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

    #kernel (vertically and horizontally)
    kernel_v = np.array([[0, -1, 0], [0, 1, 0], [0, 0, 0]]).astype(np.float32)
    kernel_h = np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]]).astype(np.float32)

    #filtering (vertically and horizontally)
    out_v = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)
    out_h = np.zeros((H+pad*2, W+pad*2, C)).astype(np.float32)

    for y in range(H):
        for x in range(W):
            for c in range(C):
                region = img_pad[y:y+k_size, x:x+k_size, c]
                out_v[y+pad, x+pad, c] = np.sum(region * kernel_v)
                out_h[y+pad, x+pad, c] = np.sum(region * kernel_h)

    #padding除去
    out_v = out_v[pad:H+pad, pad:W+pad]
    out_h = out_h[pad:H+pad, pad:W+pad]

    #下限上限
    out_v = np.clip(out_v, 0, 255)
    out_h = np.clip(out_h, 0, 255)

    return out_v, out_h


img = cv2.imread("imori.jpg").astype(np.float32)

img_gray = BGR2gray(img)

out_v, out_h = differential_filter(img_gray)
out_v = out_v.astype(np.uint8)
out_h = out_h.astype(np.uint8)

cv2.imwrite(r"out/out_14_v.jpg", out_v)
cv2.imshow("", out_v)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite(r"out/out_14_h.jpg", out_h)
cv2.imshow("", out_h)
cv2.waitKey(0)
cv2.destroyAllWindows