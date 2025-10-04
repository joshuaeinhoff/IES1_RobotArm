# IES1_RobotArm
Working with the Elephant Robotics MyCobot 6D Robot Arm. 

The main part of the code are two tracking files.
- robot-face-tracking.py
- robot-hand-tracking.py

OpenCV was used to implement live face and hand tracking from video captured by a USB webcam. The robot arm movement was decided by a very primitive algorithm based on the position of the finger tip or the center of the face.

Although there is code for a website in this repository, if I remember correctly, I ultimately decided to make a GUI with Tkinter. Sadly, that code is no longer available.

This project was created for the course Integrated Exercise for Systems 1 at the University of Aizu.
