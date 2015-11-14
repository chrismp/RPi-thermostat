# External module imports
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Pin Definitons:
acPin =  22
fanPin = 23
thermometerPin = 4

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(acPin, GPIO.OUT) # AC pin set as output
GPIO.setup(fanPin, GPIO.OUT)
GPIO.output(acPin,GPIO.HIGH)
GPIO.output(fanPin,GPIO.HIGH)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        # print 'Trying to grab temperature and humidity'
        humidity, temperature = Adafruit_DHT.read_retry(sensor, thermometerPin)
        tempF = temperature * 9/5.0 + 32

        # Note that sometimes you won't get a reading and
        # the results will be null (because Linux can't
        # guarantee the timing of calls to read the sensor).  
        # If this happens try again!
        if humidity is not None and temperature is not None:
            print 'Temp={0:0.1f}*C/{1:0.1f}*F  Humidity={2:0.1f}% -- {3}'.format(temperature, tempF, humidity, time.ctime())
            if tempF > 80:
                print "Air conditioner and fan ON"
                GPIO.output(acPin, GPIO.LOW)
                GPIO.output(fanPin, GPIO.LOW)
            else:
                print "Air conditioner and fan OFF"
                GPIO.output(acPin, GPIO.HIGH)
                GPIO.output(fanPin, GPIO.HIGH)                    
        else:
            print 'Failed to get reading. Try again!'

        time.sleep(5)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
