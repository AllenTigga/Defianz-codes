import tkinter as tk
from tkinter import ttk
from tkinter import *
import rospy
import time
from std_msgs.msg import Int16

class Display_Sensor_1(tk.Tk):

    def __init__(self):
        super().__init__()
        self.sub = rospy.Subscriber("/front_angle_low_res", Int16, self.callback_sensor_1)
        self.sensor_1_data = tk.IntVar()

        # configure the root window
        self.title('Sensor 1 Data')
        self.resizable(0, 0)
        self.geometry('640x480')
        self['bg'] = 'black'
        self.attributes('-fullscreen', True)
        
        self.canvas=Canvas(self, width=640, height=480)
        self.canvas.place(x=-2,y=-2)
        self.img= PhotoImage(file="hug.png")
        self.canvas.create_image(2,2,image=self.img,anchor=NW)
     
        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure('TLabel', background='black', foreground='red')
        self.label = ttk.Label(self, text=self.get_sensor_data(), font=('Digital-7', 20))
        self.label.pack(expand=True)
        self.label.after(1000, self.update)     # schedule an update every 1 second

    def callback_sensor_1(self, data):   
        self.sensor_1_data = data.data
        #print(self.sensor_1_data)
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    def get_sensor_data(self):
        return self.sensor_1_data

    def update(self):
        """ update the label every 1 second """
        self.label.configure(text=self.get_sensor_data())
        self.label.after(1000, self.update)     # schedule another timer
 
if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    sensor = Display_Sensor_1()
    sensor.mainloop()
