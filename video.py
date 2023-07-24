import cv2

vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('frame', rotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
vid.release()
cv2.destroyAllWindows()

