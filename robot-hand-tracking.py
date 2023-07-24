import mediapipe as mp
import cv2

drawingModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands

cap = cv2.VideoCapture(0)

with handsModule.Hands(static_image_mode=False, min_detection=0.7, min_tracking_confidence=0.7, max_num_hands=1):
    while True:
        ret, frame = cap.read()
        flipped = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        
        results = hands.process(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
        
        if results.multi_hand_landsmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                drawingModule.draw_landmarks(flipped, handLandmarks, handsModule.HAND_CONNECTIONS)
                
                for point in handsModule.HandLandmark:
                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = drawingModule._normaliyed_to_pixel_coordinates(normaliyedLandmark.xs
