#1/usr/bin/python

import time
import RPi.GPIO as GPIO

print GPIO.VERSION
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

def interrupt_fired(channel):
    print("interrupt Fired")
    print(channel)

GPIO.add_event_detect(4,GPIO.FALLING, callback=interrupt_fired)

while(True):
    time.sleep(1)
    print("timer fired")
```
## pir 센서 코드 최종 완성본
```
  1 #1/usr/bin/python
  2
  3 import time
  4 import RPi.GPIO as GPIO
  5 import Adafruit_DHT
  6 import time
  7 import requests, json
  8 from influxdb import InfluxDBClient as influxdb
  9
 10 print GPIO.VERSION
 11 GPIO.setmode(GPIO.BCM)
 12 GPIO.setup(4,GPIO.IN)
 13
 14 def interrupt_fired(channel):
 15     print("interrupt Fired")
 16     print(channel)
 17     a=5
 18     data = [{
 19         'measurement':'pir',
 20         'tags':{
 21             'VisionUni':'2410',
 22             },
 23         'fields':{
 24             'pir': a,
 25             }
 26         }]
 27     client = None
 28     try:
 29         client = influxdb('localhost',8086,'root','root','pir')
 30     except Exception as e:
 31         print "Exception" + str(e)
 32     if client is not None:
 33         try:
 34             client.write_points(data)
 35         except Exception as e:
 36             print "Exception write" + str(e)
 37         finally:
 38             client.close()
 39
 40 GPIO.add_event_detect(4,GPIO.FALLING, callback=interrupt_fired)
 41
 42 while(True):
 43     time.sleep(1)
 44     a=1
 45     data = [{
 46         'measurement':'pir',
 47         'tags':{
 48             'VisionUni':'2410',
 49             },
 50         'fields':{
 51             'pir': a,
 52             }
 53         }]
 54     client = None
 55     try:
 56         client = influxdb('localhost',8086,'root','root','pir')
 57     except Exception as e:
 58         print "Exception" + str(e)
```
