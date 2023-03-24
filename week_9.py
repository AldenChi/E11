import RPi.GPIO as GPIO
import time
import datetime
import csv
import sys
import argparse

rtime = int(120)
curtime = int(time.time())
ctime = int(time.time())

#GPIO set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# main variable
count = 0

# callback
def count_pulse(channel):
    global count
    count += 1
    print(time.time())

# callback function
GPIO.add_event_detect(26, GPIO.FALLING, callback=count_pulse)

meta_data = ["Time","Count"]
f = open("4Al_radiation_count.csv","w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)

tetime=0
while ctime < curtime+rtime:
    curtime=int(curtime)
    ctime = int(time.time())
    try:
        count = 0
        time.sleep(10)
        print("Counts in 10 seconds:", count)
        tetime=tetime+10
        data = [tetime,count]
        writer.writerow(data)
    except KeyboardInterrupt:
        # Clean up GPIO 
        GPIO.cleanup()
        data = [time.time(),count]
        writer.writerow(data)
print("Counts this minute:", count) 
f.close()
