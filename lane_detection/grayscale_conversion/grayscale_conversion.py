import cv2
import numpy as np
import pygame
import sys
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()


def hough_transform(original, canny_edge_frame):
    lines = cv2.HoughLinesP(canny_edge_frame, 1, np.pi / 180, 100, 300, 10)
    if lines is not None:
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                cv2.line(original, (x1, y1), (x2, y2), (255, 0, 0), 2)


def cv2pygame(img):
    img = np.rot90(img)
    img = pygame.surfarray.make_surface(img)
    return img


def to_grayscale(bgr_frame):
    return cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)


def to_rgb(bgr_frame):
    return cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)


def canny_edge(grayscale_frame):
    return cv2.Canny(grayscale_frame, 200, 10)


vertices = np.array([[0, 1080], [0, 540], [1920, 540], [1920, 1080]], np.int32)


def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, [vertices], WHITE)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked


cap = capture = cv2.VideoCapture('drive.mp4')


try:
    while cap.isOpened():
        ret, frame = cap.read()
        height, width, layers = frame.shape
        frame = roi(frame, vertices)
        grayscale_frame = to_grayscale(frame)
        canny_frame = canny_edge(grayscale_frame)
        hough_transform(frame, canny_frame)
        screen.blit(cv2pygame(frame), (0, 0))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

except KeyboardInterrupt:
    cv2.destroyAllWindows()
