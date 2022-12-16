import time
import serial
from tkinter import *
import math
import continuous_threading
root=Tk()
root.title("Defianz_DashBoard")
root.geometry("800x480")
root.minsize(800,480)
canvas=Canvas(root, width=800, height=480)
canvas.place(x=-2,y=-2)
img= PhotoImage(file="hug.png")
canvas.create_image(2,2,image=img,anchor=NW)

arduinoData=serial.Serial('com5',9600)
time.sleep(1)
# Speed
speed_label=Label(text="0",fg="#5271FF",bg="#272337",font=("Glacial Indifference",40,"bold"))
speed_label.place(x=180,y=130)
# Speed_needle
speed_dial_size = 100
x = 210
y = 200
x2 = x + speed_dial_size * math.sin((0/30)+4.32)
y2 = y - speed_dial_size * math.cos((0/30)+4.32)
needle = canvas.create_line(x, y, x2, y2, fill="green", width=4)

# Rpm
Rpm_label=Label(text="0",fg="#5271FF",bg="#272337",font=("comicansms",30,"bold"))
Rpm_label.place(x=180,y=280)

def delete_speed_dial(values):
    canvas.delete(values)

def update_data():
    # while (arduinoData.inWaiting()==0):
    #     pass
    dataPacket=arduinoData.readline()
    dataPacket=dataPacket.decode("utf-8")
    dataPacket=dataPacket.strip('\r\n')
    dataPacket=dataPacket.split(',')
    # updating speed needle
    global needle
    speed_dial_size = 100
    # x = 210
    # y = 200
    # x2 = x + speed_dial_size * math.sin((int(dataPacket[1]) / 30) + 4.32)
    # y2 = y - speed_dial_size * math.cos((int(dataPacket[1]) / 30) + 4.32)
    delete_speed_dial(needle)
    needle = canvas.create_line(x, y, x2, y2, fill="green", width=4)
    # updating Rpm
    # updating speed_label
    speed_label.config(text=dataPacket[1])
    Rpm_label.config(text=dataPacket[1])
    # Volt_label.config(text=dataPacket[2])
    # Current_label.config(text=dataPacket[3])
    # motor_label.config(text=dataPacket[4])
    # accuator_label.config(text=dataPacket[5])
    print(dataPacket)

t1 = continuous_threading.PeriodicThread(.1, update_data)
t1.start()
root.mainloop()








