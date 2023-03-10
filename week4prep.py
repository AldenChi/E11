# -*- coding: utf-8 -*-
"""Week4prep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FJV_SQL8obRlRgljM7x6xxyIBmfGlvl8
"""

import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C

un=int(time.time())
timr=un+30

reset=None

import serial
uart=serial.Serial("/dev/ttyS0", baudrate=9600,timeout=0.25)

from adafruit_pm25.uart import PM25_UART
pm25=PM25_UART(uart, reset)
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
#pm25 = PM25_I2C(i2c, reset)

print ("Found PM2.5 sensor, reading data...")
meta_data=["Time","pm10std", "pm25std","pm100std"]
import csv
f=open("data.csv", "w",newline='')
write=csv.writer(f)
write.writerow(meta_data)

z=0
while un<timr:
  time.sleep(1)
  un=int(time.time())
  t=time.time()
  z=z+1
  print('time=',1)
  try:
      aqdata=pm25.read()
      print(aqdata)
  except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
  data= [t,aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]]
  write.writerow(data)

f.close()
