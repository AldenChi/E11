import RPi.GPIO as GPIO
import time
import datetime
import csv
import sys
import argparse

rtime = len(sys.argv[0])
curtime = int(time.time())
ctime = int(time.time())

#GPIO set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# main variable
count = 0

# callback
def count_pulse(channel):
    if GPIO.input(26):
        global count
        count += 1
        print(time.time())

# callback function
GPIO.add_event_detect(26, GPIO.FALLING, callback=count_pulse)

meta_data = ["Time","Count"]
f = open("radiation_count.csv","w",newline = '')
writer = csv.writer(f)
writer.writerow(meta_data)

while ctime < curtime+rtime:
    ctime = int(time.time())
    try:

        count=count
        
        time.sleep(60)
        print("Counts this minute:", count)
    except KeyboardInterrupt:
        # Clean up GPIO 
        GPIO.cleanup()
    data = [time.time(),count]
    writer.writerow(data)
    
f.close()
