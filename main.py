import formic

import Laczenie
import Wczytanie
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time
v1, width, height = Wczytanie.Wczytani('Json_file.json')
heighttab = np.array(height)
widthtab = np.array(width)
images = np.array
for i in range(len(v1)):
    v1tab = np.array(v1[i])
    v1pic = v1tab.reshape((heighttab[i],widthtab[i]))
    width = int(widthtab[i])
    height = int(heighttab[i])
    dim = (width, height)
    img = cv2.resize(v1pic, dim, interpolation = cv2.INTER_NEAREST)
    plt.imshow(img, cmap='gray')
    plt.show()

