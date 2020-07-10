#1/usr/bin/python

import sys, serial, time
import requests, json
from influxdb import InfluxDBClient as influxdb

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)


comm='/dev/ttyAMA0'
baudrate=38400

device=serial.Serial(comm, baudrate, timeout= 5)
print(device)

while(True):
    try:
        rcvBuf = bytearray()
        device.reset_input_buffer()
        rcvBuf = device.read_until(size=12)
        print rcvBuf
        temp=rcvBuf.find('p')
        a=rcvBuf[2:temp]
        b=int(a)
        data = [{

        'measurement':'pir',

        'tags':{

            'VisionUni':'2410',

            },

        'fields':{

            'co2': b,

            }

        }]

        client = None
        client = influxdb('localhost',8086.'root','root','co2')
        if client is not None:
            try:
            client.write_points(data)
            
            except Exception as e:
            print "Exception write" + str(e)
            
            finally:
                client.close()

    except Exception as e:
        print("Exception read") + str(e)

    time.sleep(5)

