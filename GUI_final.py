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
        
        self.accumulator_temp_data = tk.IntVar()
        self.battery_current_data = tk.IntVar()
        self.motor_controller_temp_data = tk.IntVar()
        self.thermistor_temp_max_data = tk.IntVar()
        
        #int8 dtc_1
        #int8 dtc_2
        #bool lv_battery_status
# _0label=canvas.create_text(x*.33,55,text="0",font=('Norwester',35),fill='red')
# _0needle=canvas.create_line(x*.33, 19, x*.33, 33, fill="green", width=4)
# _1label=canvas.create_text(x*.45,55,text="1",font=('Norwester',35),fill='red')
# _1needle=canvas.create_line(x*.45, 19, x*.45, 33, fill="green", width=4)
# _2label=canvas.create_text(x*.57,55,text="2",font=('Norwester',35),fill='red')
# _2needle=canvas.create_line(x*.57, 19, x*.57, 33, fill="green", width=4)
# _3label=canvas.create_text(x*.69,55,text="3",font=('Norwester',35),fill='red')
# _3needle=canvas.create_line(x*.69, 19, x*.69, 33, fill="green", width=4)
# _4label=canvas.create_text(x*.81,55,text="4",font=('Norwester',35),fill='red')
# _4needle=canvas.create_line(x*.81, 19, x*.81, 33, fill="green", width=4)
# _5label=canvas.create_text(x*.93,55,text="5",font=('Norwester',35),fill='red')
# _5needle=canvas.create_line(x*.93, 19, x*.93, 33, fill="green", width=4)

########____________#########

# my_img= PhotoImage(file="hug.png")
# Ips=canvas.create_image(2,2,image=my_img,anchor=NW)
# character = PhotoImage(file="img.png")
#
# for x in range(0,170):
#     canvas.move(Ips,0,0)
#     root.update()
#     time.sleep(0.005)
# canvas.delete(Ips)

        # configure the root window
        self.title('Sensor 1 Data')
        self.resizable(0, 0)
        self.geometry('640x480')
        self['bg'] = 'black'
        #self.attributes('-fullscreen', True)
        
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
        
        self.accumulator_temp_label = ttk.Label(self, text=self.accumulator_temp_sensor_data(), font=('Digital-7', 20))
        self.accumulator_temp_label.place(x=300,y=100)
        self.battery_current_label = ttk.Label(self, text=self.battery_current_sensor_data(), font=('Digital-7', 20))
        self.battery_current_label.place(x=300,y=200)
        self.motor_controller_temp_label = ttk.Label(self, text=self.motor_controller_temp_sensor_data(), font=('Digital-7', 20))
        self.motor_controller_temp_label.place(x=400,y=100)
        self.thermistor_temp_max_label = ttk.Label(self, text=self.thermistor_temp_max_sensor_data(), font=('Digital-7', 20))
        self.thermistor_temp_max_label.place(x=400,y=200)
        
        self.rpm_label.after(1000, self.update)     # schedule an update every 1 second

    def callback(self, data):   
        self.rpm_data = data.rpm
        self.vel_data = data.vel
        self.battery_voltage_data = data.battery_voltage
        self.motor_temp_data = data.motor_temp
        
        self.accumulator_temp_data = data.accumulator_temp
        self.battery_current_data = data.battery_current
        self.motor_controller_temp_data = data.motor_controller_temp
        self.thermistor_temp_max_data = data.thermistor_temp_max

    def rpm_sensor_data(self):
        return self.rpm_data
    def vel_sensor_data(self):
        return self.vel_data
    def battery_voltage_sensor_data(self):
        return self.battery_voltage_data
    def motor_temp_sensor_data(self):
        return self.motor_temp_data
    
    def accumulator_temp_sensor_data(self):
        return self.accumulator_temp_data
    def battery_current_sensor_data(self):
        return self.battery_current_data
    def motor_controller_temp_sensor_data(self):
        return self.motor_controller_temp_data
    def thermistor_temp_max_sensor_data(self):
        return self.thermistor_temp_max_data

    def update(self):
        """ update the label every 1 second """
        self.rpm_label.configure(text=self.rpm_sensor_data())
        self.vel_label.configure(text=self.vel_sensor_data())
        self.battery_voltage_label.configure(text=self.battery_voltage_sensor_data())
        self.motor_temp_label.configure(text=self.motor_temp_sensor_data())
        
        self.accumulator_temp_label.configure(text=self.accumulator_temp_sensor_data())
        self.battery_current_label.configure(text=self.battery_current_sensor_data())
        self.motor_controller_temp_label.configure(text=self.motor_controller_temp_sensor_data())
        self.thermistor_temp_max_label.configure(text=self.thermistor_temp_max_sensor_data())
        
        self.rpm_label.after(1000, self.update)     # schedule another timer
 
if __name__ == "__main__":
    rospy.init_node('listener', anonymous=True)
    sensor = Display_Sensor()
    sensor.mainloop()
