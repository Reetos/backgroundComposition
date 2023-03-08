import cv2
video = cv2.VideoCapture("sofa.mp4")

while True:
    ret,frame = video.read()
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
