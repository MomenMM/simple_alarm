from pygame import mixer
import time
import os
import pyfiglet
from win10toast import ToastNotifier
from datetime import datetime

mixer.init()
mixer.music.load('ringtone.wav')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("hey and welcome to this simple alarm program\n time now is " + str(datetime.now().strftime("%H:%M")))
alrlong = int(input("how long do you want the alarm to play? write in seconds\n "))
snooze = int(input("how long do you want the snooze to be? write in seconds\n "))
times = int(input("how many times do you want the alarm to try again?\n "))
print("time now is " + str(datetime.now().strftime("%H:%M")))
inpt = input("please enter the time for the alarm to ring at in the format HH:MM\n")
clear()
print("alarm set for " + inpt)
time.sleep(10)
while str(datetime.now().strftime("%H:%M")) != inpt:
    print("time now is " + str(datetime.now().strftime("%H:%M")))
    time.sleep(1)
    clear()
else:
    i = 0
    while i < times:
        alring = ToastNotifier()
        mixer.init()
        mixer.music.load('ringtone.wav')
        print(pyfiglet.figlet_format("Alarm is ringing!"))
        alring.show_toast("Alarm is ringing!", "time's up!", duration=2)
        mixer.music.play(-1)
        time.sleep(alrlong)
        mixer.music.stop()
        time.sleep(snooze)
        i += 1
