from tkinter import *
import time
from tkinter import messagebox
root = Tk()

root.geometry("300x300")
root.title("Timer")
hour = StringVar()
hour.set("00")

minute = StringVar()
minute.set("00")

second = StringVar()
second.set("00")

def countdown():
    try:
        temp=(int(hour.get())*3600)+(int(minute.get())*60)+(int(second.get()))

    except:
        print("Please input a valid value")
    while temp >-1:
        mins,secs = divmod(temp,60)
        hours = 00
        if mins > 60:
            hours,mins = divmod(mins,60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))
        root.update()
        time.sleep(1)
        if temp == 0:
            messagebox.showinfo("Label",'Times Up!')
        temp = temp -1

hourEntry = Entry(root,width = 2,font=("Arial",18,"bold"),textvariable=hour)
hourEntry.place(x=80,y=20)

minuteEntry = Entry(root,width =2,font = ("Arial",18,"bold"),textvariable = minute)
minuteEntry.place(x=120,y=20)

secondEntry = Entry(root,width=2,font=("Arial",18,"bold"),textvariable = second)
secondEntry.place(x=160,y=20)

setButton = Button(root,text="Set Time Countdown",font = ("Arial",14,"bold"),command = countdown)
setButton.place(x=40,y=180)




root.mainloop()
