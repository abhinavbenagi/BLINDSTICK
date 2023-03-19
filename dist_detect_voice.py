import RPi.GPIO as GPIO
import time
from TFLite_detection_webcam_voice import obj_detect
import os
import argparse
import cv2
import numpy as np
import sys
import time

from gtts import gTTS
import os
text=''

def speak(audio):
    tts=gTTS(text=audio,lang="en")
    tts.save("audio1.mp3")
    os.system("mpg321 audio1.mp3")
    
from threading import Thread
import importlib.util
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER=18
GPIO_ECHO=24


def dist():
    while(True):
    
        print("distance measurement in progress")

        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
        GPIO.setup(GPIO_ECHO,GPIO.IN)


        print("waiting....")
        GPIO.output(GPIO_TRIGGER,True)

        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER,False)
            
        while GPIO.input(GPIO_ECHO)==0:
            StartTime=time.time() 

        while GPIO.input(GPIO_ECHO)==1:
            StopTime=time.time()

        TimeElapsed =StopTime-StartTime
        distance=(TimeElapsed*34300)/2
        distance=round(distance,2)
        print("Measure  Distance = %.1f cm" %distance)
        d= str(distance)
        
       
        print("**********************************************************")
        
        if(distance<50):
            speak("the object is at distance of"+d+"  cm")
            obj_detect()
            time.sleep(2)
            if dist.waitKey(1) == ord('q'):
                break
        else:
            dist()

        time.sleep(0)
dist()
