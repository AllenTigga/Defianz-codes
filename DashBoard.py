from tkinter import *
from tkinter import ttk
import math

root=Tk()
root.title("Defianz_DashBoard")

#root.attributes('-fullscreen', True)

root.geometry("800x480")
root.minsize(800,480)

canvas=Canvas(root, width=800, height=480)
canvas.place(x=-2,y=-2)
img= PhotoImage(file="hug.png")
canvas.create_image(2,2,image=img,anchor=NW)

#Dash board Image
#photo=PhotoImage(file="hug.png")
#image_label=Label(image=photo)
#image_label.place(x=-2,y=-2)

#button=Button(root,text='copy',width=10,command=lambda :update())
#button.pack()

#Adding Slider
############################################
def delete_speed_dial(values):
    canvas.delete(values)
speed_dial_size = 100
x = 210
y = 200
x2 = x + speed_dial_size * math.sin((0/30)+4.32)
y2 = y - speed_dial_size * math.cos((0/30)+4.32)
needle = canvas.create_line(x, y, x2, y2, fill="green", width=4)
def update_speed(values):
    global needle
    selection = str(speed.get())
    speed_label.config(text=selection)
    speed_dial_size = 100
    x = 210
    y = 200
    x2 = x + speed_dial_size * math.sin((speed.get()/30)+4.32)
    y2 = y - speed_dial_size * math.cos((speed.get()/30)+4.32)
    delete_speed_dial(needle)
    needle = canvas.create_line(x, y, x2, y2, fill="green", width=4)


speed=Scale(root,from_=0,to=120,orient=HORIZONTAL,length=200,tickinterval=30,fg="#5271FF",border=0,bg="#272337",font=("Glacial Indifference",24,"bold"),command=update_speed)
speed.place(x=0,y=500)
speed_label=Label(text="0",fg="#5271FF",bg="#272337",font=("Glacial Indifference",40,"bold"))
speed_label.place(x=180,y=130)

#################################################################
def update_Rpm(values):
    selection = str(Rpm.get())
    Rpm_label.config(text=selection)
Rpm=Scale(root,from_=0,to=10000,orient=HORIZONTAL,length=500,tickinterval=2000,fg="#5271FF",bg="#272337",font=("comicansms",24,"bold"),command=update_Rpm)
Rpm.place(x=250,y=500)
Rpm_label=Label(text="0",fg="#5271FF",bg="#272337",font=("comicansms",30,"bold"))
Rpm_label.place(x=180,y=280)

def update_Volt(values):
    selection = str(Volt.get())
    Volt_label.config(text=selection)
Volt=Scale(root,from_=0,to=300,orient=HORIZONTAL,length=200,tickinterval=150,fg="#FFDE59",border=0,bg="#1E1919",font=("Glacial Indifference",24,"bold"),command=update_Volt)
Volt.place(x=0,y=600)
Volt_label=Label(text="0",fg="#FFDE59",bg="#1E1919",font=("Glacial Indifference",12,"bold"))
Volt_label.place(x=550,y=50)

def update_Current(values):
    selection = str(Current.get())
    Current_label.config(text=selection)
Current=Scale(root,from_=0,to=300,orient=HORIZONTAL,length=200,tickinterval=150,fg="#FFDE59",border=0,bg="#1E1919",font=("Glacial Indifference",24,"bold"),command=update_Current)
Current.place(x=250,y=600)
Current_label=Label(text="0",fg="#FFDE59",bg="#1E1919",font=("Glacial Indifference",12,"bold"))
Current_label.place(x=550,y=80)

def update_motor(values):
    selection = str(motor.get())
    motor_label.config(text=selection)
motor=Scale(root,from_=0,to=120,orient=HORIZONTAL,length=200,tickinterval=50,fg="#FF1616",border=0,bg="#1E1919",font=("Glacial Indifference",24,"bold"),command=update_motor)
motor.place(x=0,y=700)
motor_label=Label(text="0",fg="#FF1616",bg="#1E1919",font=("Glacial Indifference",12,"bold"))
motor_label.place(x=550,y=200)

def update_accuator(values):
    selection = str(accuator.get())
    accuator_label.config(text=selection)
accuator=Scale(root,from_=0,to=120,orient=HORIZONTAL,length=200,tickinterval=50,fg="#FF1616",border=0,bg="#1E1919",font=("Glacial Indifference",24,"bold"),command=update_accuator)
accuator.place(x=250,y=700)
accuator_label=Label(text="0",fg="#FF1616",bg="#1E1919",font=("Glacial Indifference",12,"bold"))
accuator_label.place(x=700,y=200)


root.mainloop()
