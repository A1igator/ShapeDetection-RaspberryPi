# import the necessary packages
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

                # initialize angles
		i = approx[approx[:,:,0].argmin()][0]
		r = approx[approx[:,:,0].argmax()][0]
		t = approx[approx[:,:,1].argmin()][0]
		b = approx[approx[:,:,1].argmax()][0]

		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"

		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)

			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			if ar >= 0.95 and ar <= 1.05:
				shape = "square"
			else:
                                shape = "rectangle"


		# otherwise, we assume the shape is a circle if it has more than 6 vertices and the angles match up
		elif (abs(i[1]-r[1])<60 and abs(t[0]-b[0])<60) and len(approx) >6:
			shape = "circle"

		# return the name of the shape
		return shape
