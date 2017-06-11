#Tested in ubuntu 
#check for "winsound module" of python to generate buzz in windows os

from time import *
import subprocess
from os import *

def buzz(total_interval):
    sleep(total_interval)
    t_end = time() + 0.5 * 60  # play the alarm for 30 sec
    while time() < t_end:
        subprocess.call(['/usr/bin/canberra-gtk-play','--id','desktop-logout'])
        #'/usr/bin/canberra-gtk-play' will play sound from the current sound theme.
        #Check ls /usr/share/sounds/ubuntu/stereo to see which sounds are supported by ubuntu 

def setAlarm():
    print("This clock uses 24-hr format")
    total_sec = 0
    count = 0
    hr = int(input("Enter hour(in 24hr-format):"))
    mi = int(input("Enter minute:"))

    if(hr >= 24 or hr < 0 or mi >=60 or mi < 0):
        count += 1
        print("CAN'T SET ALARM. Try Again")
        if count >= 5:
            return
        setAlarm()
    else:
        curr_time = strftime("%H:%M",localtime()) # get local time
        lcurr_time = list(curr_time.split(':')) # separate that into a list for easier operation

        if mi < int(lcurr_time[1]):
            mi += 60
            hr -= 1

        mi = mi - int(lcurr_time[1])

        total_sec += mi * 60

        if (hr - int(lcurr_time[0])) < 0:
            hr = (hr - int(lcurr_time[0]) + 24)  # as it is a 24hr format clock
        else:
            hr = hr - int(lcurr_time[0])

        total_sec += hr * 3600
        buzz(total_sec);

setAlarm()
