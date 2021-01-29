# color tracker
import imutils
import cv2
import numpy as np

Lower = np.array([ 81, 227,   0])
Upper = np.array([122 ,255 ,255])
cam = cv2.VideoCapture(0)

while True:
	(grabbeb,frame) = cam.read()
	frame = imutils.resize(frame,width=600)
	blurred = cv2.GaussianBlur(frame, (21,21), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	
	mask = cv2.inRange(hsv,Lower ,Upper)
	mask = cv2.erode(mask, None,iterations=2)
	mask = cv2.dilate(mask, None,iterations=2)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	center = None
	if len(cnts)>0:
		c = max(cnts,key= cv2.contourArea)
		# radius of the circle and centroid of the circle
		((x,y),radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
		if radius >10:
			cv2.circle(frame, (int(x),int(y)), int(radius), (0,255,255),3)
			cv2.circle(frame, center, 5, (0,0,255),-1)
			if radius>100:
				print("stop")
			else:
				if (center[0]<150):
					print("right")
				elif (center[0]>450):
					print("left")
				elif (radius<100):
					print("front")
					# print(radius)
				else:
					pass
	cv2.imshow("frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break
cam.release()
cv2.destroyAllWindows()