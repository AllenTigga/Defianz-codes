import tkinter as tk
from tkinter import ttk
from tkinter import *
import rospy
import time
from bharat.msg import UI_display

class Display_Sensor_1(tk.Tk):

    def __init__(self):
        super().__init__()
        self.sub = rospy.Subscriber("/chatter", UI_display, self.callback)
        self.sensor_1_data = tk.IntVar()

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
     
        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='black', foreground='red')
        self.rpm_label = ttk.Label(self, text=self.get_rpm(), font=('Digital-7', 20))
        self.rpm_label.place(x=180,y=130)
        self.vel_label = ttk.Label(self, text=self.get_vel(), font=('Digital-7', 20))
        self.vel_label.place(x=180,y=180)
        self.rpm_label.after(1000, self.update)

    def callback(self, data):   
        self.rpm_data = data.rpm
        self.vel_data=data.rpm

    def get_rpm(self):
        return self.rpm_data
    def get_vel(self):
        return self.vel_data
    def update(self):
        """ update the label every 1 second """
        self.rpm_label.configure(text=self.get_rpm())
        self.vel_label.configure(text=self.get_vel())
        self.rpm_label.after(1000, self.update)
 
if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    sensor = Display_Sensor_1()
    sensor.mainloop()
