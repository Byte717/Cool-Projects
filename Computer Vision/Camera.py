import cv2
cam =cv2.VideoCapture(0)

while(True):
    ret, frame = cam.read()
    frame =cv2.flip(frame, 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27 or cv2.waitKey(1) & 0xFF == ord('q'):
        break
