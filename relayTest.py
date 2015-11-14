# External module imports
import RPi.GPIO as GPIO
import time



# Pin Definitons:
acPin =  22
fanPin = 23
# gndPin = 18
# vccPin = 22

# dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(acPin, GPIO.OUT) # AC pin set as output
GPIO.setup(fanPin, GPIO.OUT)
GPIO.output(acPin,GPIO.HIGH)
GPIO.output(fanPin,GPIO.HIGH)
# GPIO.setup(gndPin, GPIO.OUT)
# GPIO.setup(vccPin, GPIO.OUT)
# pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
# GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for AC and fan:
# print("Here's the initial state")
# GPIO.output(acPin, GPIO.LOW)
# GPIO.output(fanPin, GPIO.HIGH)
# pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        # if GPIO.input(vccPin): # button is released
            # pwm.ChangeDutyCycle(dc)
            # GPIO.output(acPin, GPIO.LOW)
        # else: # button is pressed:
            # pwm.ChangeDutyCycle(100-dc)
            # GPIO.output(vccPin, GPIO.HIGH)
            # GPIO.output(gndPin, GPIO.LOW)
            GPIO.output(acPin, GPIO.LOW)
            time.sleep(1)
            GPIO.output(fanPin, GPIO.LOW)
            time.sleep(1)
            GPIO.output(acPin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(fanPin, GPIO.HIGH)
            time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    # pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
