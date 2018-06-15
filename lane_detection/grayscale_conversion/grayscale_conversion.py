import cv2
import matplotlib.pyplot as plt
img = cv2.imread("dog.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
#plt.imshow(gray_image, cmap="gray", vmin=0, vmax=255)
#plt.show()


edges = cv2.Canny(gray_image, 100, 10)
plt.imshow(edges, cmap="gray", vmin=0, vmax=255)
plt.show()