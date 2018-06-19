import cv2
import numpy as np
import pygame
import sys
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
img = cv2.imread("lanes.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


edgy_image = cv2.Canny(gray_image, 200, 10)

lines = cv2.HoughLinesP(edgy_image, 1, np.pi/180, 100, 300, 10)
for x in range(0, len(lines)):
    for x1, y1, x2, y2 in lines[x]:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

gray_scale_rgb = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)


def cv2pygame(img):
    img = np.rot90(img)
    img = pygame.surfarray.make_surface(img)
    return img




try:
    while True:
        screen.blit(cv2pygame(rgb_img), (0, 0))
        screen.blit(cv2pygame(gray_scale_rgb), (480, 0))
        screen.blit(cv2pygame(edgy_image), (960, 0))
        screen.blit(cv2pygame(img), (1440, 0))
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

except KeyboardInterrupt:
    cv2.destroyAllWindows()
