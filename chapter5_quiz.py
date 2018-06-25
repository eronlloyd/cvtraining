# USAGE
# python chapter5_quiz.py

# import the necessary packages
import numpy as np
import cv2

# initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
canvas = np.zeros((300, 300, 3), dtype = "uint8")

# loop over the image in 10 pixel blocks
for (row, y) in enumerate(range(0, 300, 10)):
	for (col, x) in enumerate(range(0, 300, 10)):
		# initialize the color as red
		color = (0, 0, 255)

		# check to see if BOTH the row and column are
		# even or odd, and if so, update the background
		# color
		if row % 2 == col % 2:
			color = (0, 0, 0)

		# draw a 10x10 rectangle
		cv2.rectangle(canvas, (x, y), (x + 10, y + 10),
			color, -1)

# draw a green circle at the center of the image
cv2.circle(canvas, (150, 150), 50, (0, 255, 0), -1)

# show the output image
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)