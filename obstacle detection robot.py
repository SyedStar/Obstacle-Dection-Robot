import RPi.GPIO as GPIO                    #Import GPIO library
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers

TRIG = 17
ECHO = 27
led = 22
i1=16
i2=12
i3=21
i4=20

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input
GPIO.setup(led,GPIO.OUT)                  
GPIO.setup(i1,GPIO.OUT)
GPIO.setup(i2,GPIO.OUT)
GPIO.setup(i3,GPIO.OUT)
GPIO.setup(i4,GPIO.OUT)
GPIO.output(led, 1)


def ultra_sonic():
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print ("Waitng For Sensor To Settle")
  time.sleep(1)                            #Delay of 2 seconds
  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse
  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 
  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points
  if distance > 2 and distance < 15:      #Check whether the distance is within range
    print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
    distance=distance-0.5
    return 1
  else:
    print ("Out Of Range") 
    return 0

def stop():
    print ("stop")
    GPIO.output(i1, 0)
    GPIO.output(i2, 0)
    GPIO.output(i3, 0)
    GPIO.output(i4, 0)

def forward():
    GPIO.output(i1, 0)
    GPIO.output(i2, 1)
    GPIO.output(i3, 0)
    GPIO.output(i4, 1)
    print ("Forward")

def left():
    GPIO.output(i1, 0)
    GPIO.output(i2, 0)
    GPIO.output(i3, 1)
    GPIO.output(i4, 0)
    print ("left")



while True:
 try:
  u=ultra_sonic()
  print(u)
  if u == 0:
   forward()
   print("Going Forward") 
  elif u == 1:
   left()
   print("taking left")
   time.sleep(1.5)
   stop()
 except KeyboardInterrupt:
  stop()
  break
















