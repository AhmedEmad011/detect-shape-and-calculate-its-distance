import cv2 as cv
import numpy as np
import utils

# Function to be called when trackbar values change
def empty(value):
    pass

# Set window dimensions
frameWidth = 640  # Define width for resizing
frameHeight = 480  # Define height for resizing

# Create a named window for the result
cv.namedWindow("Result")  # Create a window named "Result"
cv.resizeWindow("Result", frameWidth, frameHeight + 100)

# Create the brightness trackbar
cv.createTrackbar("Brightness", "Result", 100, 255, empty)

wbecam = False  # Set to True to use webcam, or False to use image file
cap = cv.VideoCapture(0) if wbecam else None

if wbecam: 
    cap.set(10, 160)  # Set brightness
    cap.set(3, 1920)  # Set width
    cap.set(4, 1080)  # Set height

path = 'object_measurement/image1.jpeg'  # Corrected the path separator
while True:
    if wbecam:
        flag, img = cap.read()
        if not flag:  
            print("Failed to capture image from webcam")
            break
    else:
        img = cv.imread(path)
        if img is None: 
            print("Failed to load image from path")
            break

    # Get brightness value from trackbar
    brightness = cv.getTrackbarPos("Brightness", "Result")

    # Adjust brightness of the image
    img = cv.convertScaleAbs(img, alpha=1, beta=brightness - 100)  # Adjusting brightness

    # Get contours and draw on the image
    utils.get_contours(img)


    cv.imshow('Result', img)  # Display processed image in "Result" window

    # Exit the loop when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

if wbecam:
    cap.release()  # Release webcam if it was used
cv.destroyAllWindows()  # Close all OpenCV windows
