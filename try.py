import time
import cv2
import mediapipe as mp
from pyautogui import click
import os
import webbrowser as web
import keyboard
import tkinter
from math import *


# Function to detect hand gestures
# Function to detect hand gestures
def detect_gesture(hand_landmarks):
    # Get landmarks for thumb and index finger
    thumb_tip = hand_landmarks[4]
    index_tip = hand_landmarks[8]
    middle_tip = hand_landmarks[12]
    ring_tip = hand_landmarks[16]
    little_tip = hand_landmarks[20]

    # Extract x and y coordinates of thumb tip and index finger tip
    thumb_tip_x, thumb_tip_y = thumb_tip.x, thumb_tip.y
    index_tip_x, index_tip_y = index_tip.x, index_tip.y
    ring_tip_y = ring_tip.y
    middle_tip_y = middle_tip.y


    # Calculate the distance between thumb and index fingerṇ
    distance = index_tip_y - thumb_tip_y  # Use y-coordinate difference for simplicity
    distancex = thumb_tip_x -index_tip_x  
    water_distance = ring_tip_y - middle_tip_y

    #ṇṇ Define thresholds for thumbs-up and thumbs-down gestures
    thumbs_up_threshold = 0.25
    thumbs_down_threshold = -0.25
    water_threshold = 0.15
        
    # Check for thumbs-up and thumbs-down gestures based on distance
    
    if distance < thumbs_down_threshold:
        web.open("https://youtube.com/")
        web.open("https://web.whatsapp.com/")
        web.open("https://studentweb.vidyamandir.com/learn")
        time.sleep(1)
        return "Thumbs Down"
    elif water_distance>water_threshold:
        keyboard.press_and_release("alt+tab" )
        time.sleep(1.5)
        return "water style"
    elif middle_tip.y<index_tip.y<little_tip.y<thumb_tip.y:
        click(x=546, y=480)
        time.sleep(1)
        return "Play/Pause"
    elif (index_tip_x-thumb_tip_x)>0.12:
        keyboard.press_and_release("right")
        time.sleep(0.75)
        return "Right"
    elif (index_tip_x-thumb_tip_x)<(-0.12):
        keyboard.press_and_release("left")
        time.sleep(0.75)
        return "Left"
    elif (thumb_tip.y-little_tip.y)<(-0.30):
        keyboard.press_and_release("alt + f4")
        time.sleep(1.2)
        return "uda do"
    
        
    else:
        return "None"


# Main function 
def main():
    # Open camera
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Initialize MediaPipe hand detection
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

    while True:
        # Read frame from camera
        ret, frame = cap.read()

        # Check if the frame was read successfully
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the BGR image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hand landmarks
        results = hands.process(frame_rgb)

        # Check if hand landmarks are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Pass hand landmarks to detect_gesture function
                gesture = detect_gesture(hand_landmarks.landmark)

                # Display gesture text on the frame
                cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Hand Gestures", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
