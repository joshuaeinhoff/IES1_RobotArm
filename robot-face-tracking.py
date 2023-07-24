from pymycobot.mycobot import MyCobot
import time
import cv2
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
mc = MyCobot('/dev/ttyAMA0', 115200)

hrotation = 0.0
vrotation = 0.0

vrotation2 = 0.0

def setWebcamPosition():
    global hrotation
    hrotation = -90
    global vrotation
    vrotation = -90
    global vrotation2
    vrotation2 = 0
    mc.send_angles([0, 0, (-85.0), (vrotation2), (vrotation), (hrotation)],75)
    
def setSleepPosition():
    global hrotation
    hrotation = 44
    global vrotation
    vrotation = 0
    global vrotation2
    vrotation2 = 143
    mc.send_angles([0,119,(-146),vrotation2,vrotation,hrotation], 25)
    
def setHeadRotationHorizontal(angle):
    global vrotation
    global vrotation2
    mc.send_angles([0, 0, (-85.0), 0, (vrotation), (angle)],100)
    
def setHeadRotationVertical(angle):
    global hrotation
    mc.send_angles([0, 0, (-85.0), 0, (angle), (hrotation)],100)
    
def setRotation(vr2, vr, hr):
    mc.send_angles([0, 0, (-85.0),(vr2),(vr),(hr)],100)
    
def setLampPosition():
    global hrotation
    global vrotation
    hrotation = -40
    vrotation = 5.62
    global vrotation2
    vrotation2 = -26.71
    mc.send_angles([(-6.85), (-29.7), (-33.75), (vrotation2), vrotation, (hrotation)],75)
    
def playIdleAnimationStartUp():
    global hrotation
    global vrotation
    global vrotation2
    mc.send_angles([(-42.53), (-75.41), 120.32, 42.01, 90.61, (-49.65)], 70)
    time.sleep(1)
    mc.send_angles([(-153.98), (-99.4), 99.75, (-89.38), (-89.91), (-49.39)], 70)
    time.sleep(1)
    mc.send_angles([(-119.26), 11.68, 85.78, 32.08, (-94.04), (-49.39)], 70)
    time.sleep(1)
    mc.send_angles([(-19.59), (-90.87), 3.69, (-8.52), (-85.86), (-49.48)], 70)
    time.sleep(1)
    mc.send_angles([(-2.1), 1.23, 89.2, (-8.78), (-92.9), (-49.21)], 70)
    time.sleep(1)
    mc.send_angles([(-42.53), (-75.41), 120.32, 42.01, 90.61, (-49.65)], 70)
    time.sleep(1)
    hrotation = -49.65
    vrotation = 90.61
    vrotation2 = 42.01
    
    
def cameraTracking(img, x, y, w, h):
    xCenterPoint = (x + (x+w))/2
    yCenterPoint = (y + (y+h))/2
    global hrotation
    global vrotation
    global vrotation2
    #print("Face center point coords: x={}, y={}".format(xCenterPoint,yCenterPoint))
    print(mc.get_angles())
    cv2.circle(img,(int(xCenterPoint), int(yCenterPoint)), 5, (0,0,255), -1)
    if xCenterPoint < 300 & hrotation > -170:
        print("condition hit go left")
        hrotation += 1
        setHeadRotationHorizontal(hrotation)
    elif xCenterPoint > 440:
        print("condition hit go right")
        hrotation -= 1
        setHeadRotationHorizontal(hrotation)
        
    if yCenterPoint < 170:
        print("condition hit go down")
        if vrotation > -170:
            vrotation -= 1
            setHeadRotationVertical(vrotation)
    elif yCenterPoint > 300:
        print("condition hit go up")
        if vrotation < 170:
            vrotation += 1
            setHeadRotationVertical(vrotation)
            
            
def faceCamMode():
    while True:
        _, img = cap.read()
        #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        
        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #print("Face coordinates: x={}, y={}, w={}, h={}".format(x,y,w,h))
            
            cameraTracking(img,x,y,w,h)

            
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
    cap.release()

# =-=-=-=-=-=-=-=-=-=-= execution =-=-=-=-=-=-=-=-=-=-=

setSleepPosition()
print("Waiting for 5 seconds")
time.sleep(1)
print("> 1")
time.sleep(1)
print("> 2")
time.sleep(1)
print("> 3")
time.sleep(1)
print("> 4")
time.sleep(1)
print("> 5")
playIdleAnimationStartUp()
print("Playing idle animation")
print("Waiting for 7 seconds")
time.sleep(1)
print("> 1")
time.sleep(1)
print("> 2")
time.sleep(1)
print("> 3")
time.sleep(1)
print("> 4")
time.sleep(1)
print("> 5")
time.sleep(1)
print("> 6")
time.sleep(1)
print("> 7")

setWebcamPosition()
print("Waiting for positioning")
while True:
    if mc.is_moving() == 0:
        break
faceCamMode()

setSleepPosition()

