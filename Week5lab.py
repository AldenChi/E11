#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import random
import time
import argparse
import csv
import adafruit_bme680
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
    
    

i2c=board.I2C()
bme680=adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.sea_level_pressure=1013.25
     
    

reset=None

     


import serial
uart=serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.95)

     


from adafruit_pm25.uart import PM25_UART
pm25=PM25_UART(uart,reset)

     


import csv
meta_data=["Time", "PM10 std", "PM25 std", "PM100 std", "Temperature", "Gas", "Pressure", "Altitude", "Relative Humididty"]
f=open("sensor_data.csv", "w", newline='')
writer=csv.writer(f)
writer.writerow(meta_data)
print(sys.argv)
start=int(time.time())
run=int(sys.argv[1])
itime=start
     


while itime<(start+run):
  

