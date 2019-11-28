import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

redBajo1 = np.array([0,100,20],np.uint8)
redAlto1 = np.array([8,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)

amarilloBajo = np.array([15,100,20],np.uint8)
amarilloAlto = np.array([45,255,255],np.uint8)

naranja = np.array([28,89,94],np.uint8)

while (True):
    ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    if ret == True:
        frameHSV = cv2.cvtColor (frame,cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
        maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
        maskAma = cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
        maskRed = cv2.add(maskRed1,maskRed2)
        maskRedvis = cv2.bitwise_and(frame,frame, mask = maskRed)
        _,contornos,_ = cv2.findContours(maskRed,cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame,contornos, -1, (255,0,0), 3)
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 1000:
                M = cv2.moments(c)
                if (M["m00"]==0):M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int (M['m01']/M['m00'])
                cv2.circle(frame,(x,y),7,(0,255,0),-1)
                font = cv2.FONT_HERSHEY_SIMPLEX
               # cv2.putText(frame,'{},{}',format(x,y),(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame,[nuevoContorno], 0, (255,0,0), 3)
        #cv2.imshow('maskRedvis',maskRedvis)
        #cv2.imshow('maskRed',maskRed)

    cv2.imshow('video1', frame)

    if ret1 == True:
        frameHSV = cv2.cvtColor (frame1,cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
        maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
        maskAma = cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
        maskRed = cv2.add(maskRed1,maskRed2)
        maskRedvis = cv2.bitwise_and(frame1,frame1, mask = maskRed)
        _,contornos,_ = cv2.findContours(maskRed,cv2.RETR_EXTERNAL,
                                         cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame,contornos, -1, (255,0,0), 3)
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 3000:
                M = cv2.moments(c)
                if (M["m00"]==0):M["m00"]=1
                x = int(M["m10"]/M["m00"])
                y = int (M['m01']/M['m00'])
                cv2.circle(frame1,(x,y),7,(0,255,0),-1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(frame,'{},{}',format(x,y),(x+10,y),font,0.75,(0,255,0),1,cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame1,[nuevoContorno], 0, (255,0,0), 3)
        #cv2.imshow('maskRedvis',maskRedvis)
        #cv2.imshow('maskRed',maskRed)

    cv2.imshow('video2', frame1)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
   
        break

cap.release()
cap1.release()
cv2.destroyAllWindows()
    
