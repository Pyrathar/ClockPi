#!/usr/bin/python

from tkinter import *
import time
import pyowm

root = Tk()
root.attributes('-fullscreen', True)

owm = pyowm.OWM("fb774c1b27afb4ec87a22e8dccf8f46c")
observation = owm.weather_at_place('Lynbsby,dk')
w=observation.get_weather()
temperature=w.get_temperature('celsius')['temp']


time1 = ''
clock = Label(root, font=('times', 40, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)

weather = Label(root, text=temperature,font=('times', 40, 'bold'), bg='white')
weather.pack(fill=BOTH, expand=1)


def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
root.mainloop(  )