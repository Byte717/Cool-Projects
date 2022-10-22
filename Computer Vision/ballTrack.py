from collections import deque

import numpy as np
import argparse
import cv2
import imutils
import time
import os

from imutils.video import VideoStream

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())
# Morning:(29, 86, 6), (35, 255, 255)
# afternoon:(29, 86, 6) (40, 255, 255)
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])
if not args.get("video", False):
	vs = VideoStream(src=0).start()
else:
	vs = cv2.VideoCapture(0)
time.sleep(2.0)
while True:
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
	if frame is None:
		break
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (3, 3), 0)
	hsv = cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv,greenLower, greenUpper)
	mask = cv2.erode(mask, None,	 iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	cv2.imshow ("detection", mask)
	cv2.imshow("HSV Space", hsv)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		if radius > 10:
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(255, 0, 0), 3)
			cv2.circle(frame, center, 5, (255, 255 , 255), -1)
	pts.appendleft(center)
	for i in range (1, len (pts)):
		if pts[i - 1] is None or pts[i] is None:
			continue

		thickness = int (np.sqrt (args["buffer"] / float (i + 1)) * 3)
		cv2.line (frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame, "DRS",(50,60),font,1,(0,72,255), 2, cv2.LINE_AA)
	cv2.imshow ("Frame", frame)
	key = cv2.waitKey (1) & 0xFF

	if key == 27 :
		break

if not args.get ("video", False):
	vs.stop ()

else:
	vs.release ()
cv2.destroyAllWindows ()
