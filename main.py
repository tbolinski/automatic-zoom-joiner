# My github: https://github.com/Usagi-02808 And dc: usagi.02808#0678
# Availible on https://github.com/Usagi-02808/automatic-zoom-joiner
# Created by Tymon Boliński

from datetime import time
import json
import webbrowser
import datetime
import subprocess

#Opening jsons
schedulepl = open('schedule.json')
scheduleint = open('scheduleint.json')
scheduleplg = open('scheduleg.json')
scheduleintg = open('scheduleintg.json')
lesson = open('lessons.json')
lschedulebpl = json.load(schedulepl)
lschedulebplg = json.load(scheduleplg)
lschedulebint = json.load(scheduleint)
lschedulebintg = json.load(scheduleintg)
llesson = json.load(lesson)
gender = (llesson['Lesson type']['Gender'])
lsntp = (llesson['Lesson type']["Lesson type"])
jointype = (llesson['PC settings']["Type"])
pathzm = (llesson['PC settings']["Zoom path"])

joinlesson = input('Do you want to join a meeting automatically?(Y/N) ')
joinlesson = joinlesson[:1].lower()

if gender == 'Boy':
    if lsntp == 'Pol':
        schedule = lschedulebpl
    
    if lsntp == 'Int':
        schedule = lschedulebint

if gender == 'Girl':
    if lsntp == 'Pol':
        schedule = lschedulebplg
    
    if lsntp == 'Int':
        schedule = lschedulebintg

if joinlesson != 'y' and joinlesson != 'n':
    print("Incorrect answer")
    time.sleep(10)
    exit

if joinlesson == 'y':
    #Do you need to join
    x = datetime.datetime.now()
    weekday_num = x.weekday()
    if weekday_num > 4:
        print("You don't have school today ;)")
        time.sleep(10)
        exit(0)

    weekday_tuple = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    weekday = weekday_tuple[weekday_num]

    #Part of this unnecesarry, just have it for now
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    hourmin = hour, minute
    timenowget = now.time
    current_time = now.strftime("%H:%M:%S")

    if 8 > hour or hour > 15:
        print("You don't have school now ;)")
        time.sleep(10)
        exit(0)
    
    if time(8,5) <= now.time() <= time(9,00):
        lessonid = 0
    
    if time(9,00) <= now.time() <= time(9,55):
        lessonid = 1
    
    if time(9,55) <= now.time() <= time(10,55):
        lessonid = 2

    if time(10,55) <= now.time() <= time(11,45):
        lessonid = 3

    if time(11,45) <= now.time() <= time(12,40):
        lessonid = 4

    if time(12,40) <= now.time() <= time(13,30):
        lessonid = 5
    
    if time(13,30) <= now.time() <= time(15,15):
        lessonid = 6

    print(lessonid + 1)
    print(time)
    lesson = (schedule['Schedule'][weekday][lessonid])
    zoom_id = (schedule['ZoomInfo'][lesson])
    pwd = (schedule['ZoomPass'][lesson])
    
if jointype == "off":
    subprocess.Popen([f'{pathzm}',
                  f'--url=zoommtg://zoom.us/join?confno={zoom_id}&pwd={pwd}'])

if jointype == "on":
    webbrowser.open(f"https://us04web.zoom.us/j/{zoom_id}?pwd={pwd}")