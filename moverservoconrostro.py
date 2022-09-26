import cv2
import serial
import time
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
video = cv2.VideoCapture(0)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)
while video.isOpened():
    ret, frame = video.read()
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        hh,ww = gray.shape #obtener la dimension de la escena
        cv2.line(frame,(int (ww/2),0),(int (ww/2),hh),(255,0,255),2)
        for (x, y, w, h) in faces:
            if x<ww/2:
                arduino.write(b'i')
            else:
                arduino.write(b'd')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
arduino.close()
