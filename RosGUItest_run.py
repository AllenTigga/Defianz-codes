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
        self.vel_data = tk.IntVar()
        self.battery_voltage_data = tk.IntVar()
        self.motor_temp_data = tk.IntVar()

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
        self.rpm_label.place(x=100,y=100)
        self.vel_label = ttk.Label(self, text=self.vel_sensor_data(), font=('Digital-7', 20))
        self.vel_label.place(x=100,y=200)
        self.battery_voltage_label = ttk.Label(self, text=self.battery_voltage_sensor_data(), font=('Digital-7', 20))
        self.battery_voltage_label.place(x=200,y=100)
        self.motor_temp_label = ttk.Label(self, text=self.motor_temp_sensor_data(), font=('Digital-7', 20))
        self.motor_temp_label.place(x=200,y=200)
        self.rpm_label.after(1000, self.update)     # schedule an update every 1 second

    def callback(self, data):   
        self.rpm_data = data.rpm
        self.vel_data = data.vel
        self.battery_voltage_data = data.battery_voltage
        self.motor_temp_data = data.motor_temp

    def rpm_sensor_data(self):
        return self.rpm_data
    def vel_sensor_data(self):
        return self.vel_data
    def battery_voltage_sensor_data(self):
        return self.battery_voltage_data
    def motor_temp_sensor_data(self):
        return self.motor_temp_data

    def update(self):
        """ update the label every 1 second """
        self.rpm_label.configure(text=self.rpm_sensor_data())
        self.vel_label.configure(text=self.vel_sensor_data())
        self.battery_voltage_label.configure(text=self.battery_voltage_sensor_data())
        self.motor_temp_label.configure(text=self.motor_temp_sensor_data())
        self.rpm_label.after(1000, self.update)     # schedule another timer
 
if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    sensor = Display_Sensor()
    sensor.mainloop()
