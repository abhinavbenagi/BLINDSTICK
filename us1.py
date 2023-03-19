import RPi.GPIO as GPIO
import time
from speech import speak
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER=18
GPIO_ECHO=24

st=time.time()

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

et=time.time()
print("time taken to execute",et-st)
speak("the object is at distance of"+d+"  cm")

time.sleep(1)


