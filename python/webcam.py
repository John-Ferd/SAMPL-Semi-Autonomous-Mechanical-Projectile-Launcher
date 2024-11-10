# Program entry point, when arduino is connected

import cv2
import mediapipe as mp

import serial_out
from helper import normalize_to_servo_range


mp_hands = mp.solutions.hands.Hands()
mp_drawing = mp.solutions.drawing_utils
capture = cv2.VideoCapture(0)

# Edit these values appropriately depending on the servo
SERVO_MIN = 150
SERVO_MAX = 600


while (True):
    # Store the frame from the video capture and resize it to the desired window size.
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)

    results = mp_hands.process(frame)
    image_height, image_width, _ = frame.shape

    landmark_count = 0
    x_sum = 0
    y_sum = 0

    if results.multi_hand_landmarks:
        #print("HAND FOUND")
        i = 0
        for hand_landmarks in results.multi_hand_landmarks:
            if i > 1:
                continue
            i += 1
            for ids, landmrk in enumerate(hand_landmarks.landmark):
                landmark_count += 1
                cx, cy = landmrk.x * image_width, landmrk.y*image_height
                x_sum += cx
                y_sum += cy
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
            
        #print(f"Average: {x_sum/landmark_count} {y_sum/landmark_count}")
    
        if x_sum > 0 and y_sum > 0:
            norm_x, norm_y = normalize_to_servo_range(image_width, image_height, x_sum/landmark_count, y_sum/landmark_count, SERVO_MIN, SERVO_MAX)
            serial_out.write(str(norm_x) + " " + str(norm_y))

    cv2.imshow('MediaPipe Hands', frame)

    if (cv2.waitKey(30) == 32):
        serial_out.fire()
    # Check if user wants to exit.
    if (cv2.waitKey(20) & 0xFF == ord('x')):
        break

# When we exit the loop, we have to stop the capture too
capture.release()
cv2.destroyAllWindows()