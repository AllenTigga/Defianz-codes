import tkinter as tk
from tkinter import ttk
from tkinter import *
import rospy
import time
from bharat.msg import UI_display

class Display_Sensor(tk.Tk):

    def __init__(self):
        super().__init__()
        self.sub = rospy.Subscriber("/chatter", UI_display, self.callback)
        self.rpm_data = tk.IntVar()

        # configure the root window
        self.title('Sensor 1 Data')
        self.resizable(0, 0)
        self.geometry('640x480')
        self['bg'] = 'black'
        self.attributes('-fullscreen', True)
        
        self.canvas=Canvas(self, width=640, height=480)
        self.canvas.place(x=-2,y=-2)
        self.img= PhotoImage(file="/home/pi/catkin_ws/src/bharat/Defianz-codes/hug.png")
        self.canvas.create_image(2,2,image=self.img,anchor=NW)
     
        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='black', foreground='red')
        self.rpm_label = ttk.Label(self, text=self.rpm_sensor_data(), font=('Digital-7', 20))
        self.rpm_label.place(x=250,y=500)
        self.rpm_label.after(1000, self.update)     # schedule an update every 1 second

    def callback(self, data):   
        self.rpm_data = data.vel

    def rpm_sensor_data(self):
        return self.rpm_data

    def update(self):
        """ update the label every 1 second """
        self.rpm_label.configure(text=self.rpm_sensor_data())
        self.rpm_label.after(1000, self.update)     # schedule another timer
 
if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    sensor = Display_Sensor()
    sensor.mainloop()
