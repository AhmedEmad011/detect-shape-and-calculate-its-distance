import cv2 as cv
import numpy as np

def get_contours(img, pixel_to_cm_ratio=0.1):
    # Parameters for Canny edge detection
    cThr = [10, 10]
    
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv.Canny(imgBlur, cThr[0], cThr[1])
    contours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 100:  
            perimeter = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv.boundingRect(approx)
            
            width_cm = round(w * pixel_to_cm_ratio, 1)
            height_cm = round(h * pixel_to_cm_ratio, 1)
            
            cv.arrowedLine(img, (x, y), (x + w, y), (255, 0, 255), 2, tipLength=0.05)
            cv.arrowedLine(img, (x, y), (x, y + h), (255, 0, 255), 2, tipLength=0.05)
            
            cv.putText(img, f"{width_cm}cm", (x + w // 2, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            cv.putText(img, f"{height_cm}cm", (x - 50, y + h // 2), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    
    cv.imshow('Canny', imgCanny)
