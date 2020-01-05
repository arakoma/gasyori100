import cv2
import numpy as np


def BGR2HSV(img):
    h, w, c = img.shape
    hsv = img.copy()

    for y in h:
        for x in w:
            b, g, r = img[y, x]

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