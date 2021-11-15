import cv2
import os
import sys
import pkg_resources
import glob
import RPi.GPIO as GPIO


LED_RED = 21
LED_YELLOW = 20
GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BCM)   
GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.LOW)  
GPIO.setup(LED_YELLOW, GPIO.OUT, initial=GPIO.LOW)


def get_camera_index():
    camIndex = [int(vi.split("/")[-1][5:]) for vi in glob.glob("/dev/video*")]
    for ci in camIndex:
        try:
            cap = cv2.VideoCapture(ci)
            ret, frame = cap.read()
            cap.release()
            if ret == True:
                return ci
        except:
            pass
    return None 


def main(argv=None):
    if argv is None:
        argv = sys.argv
    print("Searching for camera index")
    cindex = get_camera_index()
    if cindex is None:
        print("Camera not found")
        return 0

    GPIO.output(LED_RED, GPIO.HIGH)
    red_on = True
    yellow_on = False

    print(f"Camera at {cindex}")
    hdata = pkg_resources.resource_filename(
            "faceledapp", f"model/haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(hdata)

    cap = cv2.VideoCapture(cindex)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (256,256), interpolation = cv2.INTER_AREA)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(faces) > 0:
                if yellow_on is False:
                    GPIO.output(LED_YELLOW, GPIO.HIGH)
                    yellow_on = True

                if red_on is True:
                    GPIO.output(LED_RED, GPIO.LOW)
                    red_on = False
            else:
                if yellow_on is True:
                    GPIO.output(LED_YELLOW, GPIO.LOW)
                    yellow_on = False

                if red_on is False:
                    GPIO.output(LED_RED, GPIO.HIGH)
                    red_on = True

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0

            
