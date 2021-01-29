# color Tuning
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cv2.namedWindow("Color Tuning")

def nothing(x):
	pass

cv2.createTrackbar("Low-Hue", "Color Tuning", 0, 179, nothing)
cv2.createTrackbar("Low-Sat", "Color Tuning", 0, 255, nothing)
cv2.createTrackbar("Low-Vis", "Color Tuning", 0, 255, nothing)
cv2.createTrackbar("Upp-Hue", "Color Tuning", 179, 179, nothing)
cv2.createTrackbar("Upp-Sat", "Color Tuning", 255, 255, nothing)
cv2.createTrackbar("Upp-Vis", "Color Tuning", 255, 255, nothing)


while True:
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	l_h = cv2.getTrackbarPos("Low-Hue", "Color Tuning")
	l_s = cv2.getTrackbarPos("Low-Sat", "Color Tuning")
	l_v = cv2.getTrackbarPos("Low-Vis", "Color Tuning")

	u_h = cv2.getTrackbarPos("Upp-Hue", "Color Tuning")
	u_s = cv2.getTrackbarPos("Upp-Sat", "Color Tuning")
	u_v = cv2.getTrackbarPos("Upp-Vis", "Color Tuning")




	_low = np.array([l_h,l_s,l_v])
	_hgh = np.array([u_h,u_s,u_v])

	mask = cv2.inRange(hsv, _low, _hgh)




	cv2.imshow("frame", frame)
	cv2.imshow("hsv", hsv)
	cv2.imshow("mask", mask)



	key = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		print("Clr lower",_low)
		print("Clr Upper",_hgh)
		print("quit")
		break
cap.release()
cv2.destroyAllWindows()