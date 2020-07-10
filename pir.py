#1/usr/bin/python

import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import requests, json
from influxdb import InfluxDBClient as influxdb

print GPIO.VERSION
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

def interrupt_fired(channel):
    print("interrupt Fired")
    print(channel)
    a=5
    data = [{
        'measurement':'pir',
        'tags':{
            'VisionUni':'2410',
            },
        'fields':{
            'pir': a,
            }
        }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print "Exception" + str(e)
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print "Exception write" + str(e)
        finally:
            client.close()
        
GPIO.add_event_detect(4,GPIO.FALLING, callback=interrupt_fired)

while(True):
    time.sleep(1)
<<<<<<< HEAD
    a=1
    data = [{
        'measurement':'pir',
        'tags':{
            'VisionUni':'2410',
            },
        'fields':{
            'pir': a,
            }
        }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','pir')
    except Exception as e:
        print "Exception" + str(e)
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print "Exception write" + str(e)
        finally:
            client.close()
        print("running influxdb ok")


=======
    print("timer fired")
>>>>>>> 6f500b319920f5308839ccc5ddf12eb9911cb6dd
