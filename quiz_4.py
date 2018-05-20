import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

radius = np.random.randint(5, high=200)
color = np.random.randint(0, high=265, size=(3,)).tolist()
pt = np.random.randint(0, high=300, size=(2,))

cv2.circle(canvas, tuple(pt), radius, color, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
