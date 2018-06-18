import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("lanes.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
#plt.imshow(gray_image, cmap="gray", vmin=0, vmax=255)
#plt.show()


edges = cv2.Canny(gray_image, 200, 10)

lines = cv2.HoughLinesP(edges , 1, np.pi/180, 100, 300, 10)
for x in range(0, len(lines)):
    for x1, y1, x2, y2 in lines[x]:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.show()