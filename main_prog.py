#!/usr/bin/env python3
from os.path import dirname, realpath, join
import sys
import mod_visual.mod_visual_obj
from mod_visual.mod_visual import Marco
from mod_system.mod_sensor import freq_get, get_sensors_data, sen_get

Dir_prog = dirname(realpath(__file__))
for j in ['mod_system', 'mod_visual']:
    Dir_files = (join(Dir_prog, j))
    sys.path.append(Dir_files)

if __name__ == '__main__':
    sensor_names = sen_get()
    cpu_number = len(freq_get())
    Marco_A = Marco(cpu_number, sensor_names, 1000)
    Marco_A.func = freq_get
    Marco_A.get_value()
    Marco_A.func_sen_value = get_sensors_data
    Max_value = get_sensors_data()
    Marco_A.set_max_progress(Max_value)
    Marco_A.get_sensors_value()
    Marco_A.timer()
    Marco_A.main_loop()

