#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:
# Author:      xujuan.st@gmail.com
# Created:     01/02/2016
# Completed:   18/02/2016
# Updated:     12/03/2019
# Copyright:   (c) juan xu-msh 2016
# Licence:
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PAM31 import PAMIE
import time, re, sys

Venue = 'Anchorvale CC'
Date = "25/03/2019"

### 02:00 PM-03:00 PM -> slot_0;  03:00 PM-04:00 PM -> slot_1;
### 04:00 PM-05:00 PM -> slot_2;  05:00 PM-06:00 PM -> slot_3;
### 06:00 PM-07:00 PM -> slot_4;  07:00 PM-08:00 PM -> slot_5;
### 08:00 PM-09:00 PM -> slot_6;  09:00 PM-10:00 PM -> slot_7;
##expTime = ['02:00 PM-03:00 PM', '03:00 PM-04:00 PM']
##allTime = ['02:00 PM-03:00 PM','03:00 PM-04:00 PM','04:00 PM-05:00 PM','05:00 PM-06:00 PM',\
##           '06:00 PM-07:00 PM','07:00 PM-08:00 PM','08:00 PM-09:00 PM','09:00 PM-10:00 PM']

# 09:30 AM-10:30 AM -> slot_0;  10:30 AM-11:30 AM -> slot_1;
# 11:30 AM-12:30 PM -> slot_2;  12:30 PM-01:30 PM -> slot_3;
# 01:30 PM-02:30 PM -> slot_4;  02:30 PM-03:30 PM -> slot_5;
# 03:30 PM-04:30 PM -> slot_6;  04:30 PM-05:30 PM -> slot_7;
# 05:30 PM-06:30 PM -> slot_8;  06:30 PM-07:30 PM -> slot_9;
# 07:30 PM-08:30 PM -> slot_10; 08:30 PM-09:30 PM -> slot_11;

expTime = ['01:30 PM - 02:30 PM','02:30 PM - 03:30 PM']
allTime = ['09:30 AM - 10:30 AM','10:30 AM - 11:30 AM','11:30 AM - 12:30 PM','12:30 PM - 01:30 PM',\
           '01:30 PM - 02:30 PM','02:30 PM - 03:30 PM','03:30 PM - 04:30 PM','04:30 PM - 05:30 PM',\
           '05:30 PM - 06:30 PM','06:30 PM - 07:30 PM','07:30 PM - 08:30 PM','08:30 PM - 09:30 PM']

ie = PAMIE()

ie.navigate("https://www.onepa.sg/")
time.sleep(2)
print "Main page opened!"

raw_input('Press <ENTER> to continue')

ie.navigate("https://www.onepa.sg/facilities/4690ccmcpa-bm")
time.sleep(2)
print "Badminton Court page opened!"

ie.selectListBox("content_0$ddlFacilityLocation", Venue)
time.sleep(2)
print "Selected "+Venue+"!"

slot_count=0
try_count=0
print "Searching available time slots..."
while((slot_count==0)):
    ie.setTextBox("content_0_tbDatePicker", Date)
    calendar = ie.getElementsList("input","id=content_0_tbDatePicker")[0]
    calendar.FireEvent("onchange")
    time.sleep(2)
    try_count = try_count + 1;
    print "Refreshing vacancy for expected timeSlot, count %d" %try_count

    availCheckboxList = ie.getElementsList("input", "type=checkbox")[::-1]

    for exp in expTime:
        for act in availCheckboxList:
            print "checkBoxId="+act.id
            try:
                if (int(act.id[-1])>=0):
                    if (allTime.index(exp) == int(act.id[-1])):
                        act.click()
                        slot_count=slot_count+1
                        break
            except Exception:
                continue
        else:
            continue

print "%d slots have been booked!" % slot_count
ie.clickButton("content_0_btnAddToCart")
print "Booking done!"


