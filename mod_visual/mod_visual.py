import tkinter as tk
from tkinter import ttk
from mod_visual.mod_visual_obj import Scrollbar, Menu
from time import time, strftime
from os.path import dirname, abspath, join
import sys

Dir_prog = dirname(abspath(__file__))
sys.path.append(Dir_prog)


class Ventana():
    def __init__(self, title = 'System Monitor'):
        self.master = tk.Tk()
        self.master.title(title)
        icon = tk.PhotoImage(file = Dir_prog+'/icono_sys_mon.ico')
        self.master.iconphoto(False, icon)
        self.master.resizable(False, False)
        self.menu = Menu(self.master)


class Marco(Ventana):
    def __init__(self,cpu_num = 0, sensors = None, refresh = 1000):
        super().__init__()
        self.frame_freq_master = tk.Frame(self.master)
        self.frame_freq_master.grid(row = 0, column = 0, sticky = 'news')

        scroll_freq = Scrollbar(self.frame_freq_master)
        scroll_freq.canvas.configure(height = 200)
        self.frame = scroll_freq.sub_frame

        #Label freq. label TIT.:
        self.label_freq = tk.Label(self.frame,
                                   text = 'Frequency per Core [MHz] :',
                                   font = ('Roboto', 12))

        self.label_freq.grid(row = 0, column = 0,
                             padx = 10, pady = 10, columnspan = 2)
        #Set cpu quant. for frq SUBT.
        self.label_cpu = []
        self.entry_cpu = []
        self.__cpu_entry_count(cpu_num)
        #-----------------------------
        self.refresh = refresh

        self.frame_temp_master = tk.Frame(self.master)
        self.frame_temp_master.grid(row = 1, column = 0, padx=0,
                                    sticky = 'news')
        scroll_temp = Scrollbar(self.frame_temp_master)
        scroll_temp.canvas.configure(height = 300)
        self.frame_temp = scroll_temp.sub_frame
#-----------------------------------------------------------------------

        self.label_title = tk.Label(self.frame_temp,
                                    text = 'Temperature [C°]; Power [W]; Voltage [V]; Fan spd. [RPM] : ',
                                    font = ('Roboto', 12))
        self.label_title.grid(row = 0, column = 0, sticky = 'w',
                              padx = 10, pady = 10, columnspan = 3)
        #
        #Sensors
        self.generic_sensors_label = []
        #-------------------------
        #Label
        self.label_generic = []
        self.sensors_progres_bar = []
        self.sensors_temp_entry = []
        self.__sensors = sensors
        self.__sensors_entry_count()
        self.func = ''
        self.func_sen_value = ''
        #----------------------------------------------------------
        #Time label
        self.time_label = tk.Label(self.master)
        self.time_label.grid(row = 2, column = 0,
                             sticky='w', pady = 10, padx = 10)
        #----------------------------------------------------------


    def __cpu_entry_count(self, count):
        #Gen. entrys & label <---- /proc/cpuinfo
        for cpu in range(count):
            widget_ = tk.Label(self.frame, text = 'Freq. cpu'+str(cpu))
            widget_.grid(row = cpu+1, column = 0, padx = 10, sticky='w')
            self.label_cpu.append(widget_)
            widget_ = tk.Entry(self.frame, text = '',
                               state = 'readonly', width = 10)
            widget_.grid(row = cpu+1, column = 1, padx = 5, sticky='w')
            self.entry_cpu.append(widget_)
        return

    def __sensors_entry_count(self,):
        #Set labels/Progressbars/entrys of sensors
        #Takes dict{} argument stored in self.__sensors
        #uses

        k = 1
        for first_index, first_data in self.__sensors.items():
            widget_ = tk.Label(self.frame_temp, text = first_index)
            widget_.grid(row = k, column = 0, sticky = 'w',
                         padx = 10)

            self.generic_sensors_label.append(widget_)
            j = k+1
            for second_index, *_ in first_data.items():   #*_ data at first exec. not used
                widget_ = tk.Label(self.frame_temp, text = second_index)
                widget_.grid(row = j, column = 0, sticky = 'w',
                             padx = 10)
                self.label_generic.append(widget_)
                widget_ = ttk.Progressbar(self.frame_temp,
                                          orient = 'horizontal',
                                          length = 200,
                                          mode = 'determinate')
                widget_.grid(row = j, column = 1, padx = 5)
                self.sensors_progres_bar.append(widget_)

                widget_ = tk.Entry(self.frame_temp,
                                   state = 'readonly',
                                   width = 10)
                widget_.grid(row = j, column = 2)
                self.sensors_temp_entry.append(widget_)
                j += 1
            k +=1+j
        return

    def get_value(self, ):
        values = self.func()

        for entry, cpu_freq in zip(self.entry_cpu, values):
            entry.configure(state = 'normal')
            entry.delete(0,tk.END)
            entry.insert(0,str(cpu_freq))
            entry.configure(state = 'readonly')


        self.master.after(self.refresh, self.get_value)
        return
    def get_sensors_value(self,):
        #Print sensors value on entrys
        values = self.func_sen_value()
        for progress, sensors, vals in zip(self.sensors_progres_bar,
                                            self.sensors_temp_entry,
                                            values):
            progress.configure(value = vals[0])
            sensors.configure(state = 'normal')
            sensors.delete(0,tk.END)
            sensors.insert(0,str(vals[0]))
            sensors.configure(state = 'readonly')

        self.master.after(self.refresh, self.get_sensors_value)
        return

    def set_max_progress(self, values):
        #Set max. value --> Progressbar

        for prog,val in zip(self.sensors_progres_bar,values):
            try:
                prog.configure(maximum = val[1])

            except IndexError:

                prog.configure(maximum = 100)
        return

    def timer(self,):
        self.time_label.configure(text = strftime('System Date & Local Time:  %d-%m-%Y  @  %H:%M:%S'))
        self.master.after(self.refresh, self.timer)


    def main_loop(self,):
        self.master.mainloop()
        return

