import subprocess
import json


def freq_get():
    list_freq = subprocess.getoutput("cat /proc/cpuinfo | grep -i 'CPU MHz' | awk '{print $4}'").rsplit()
    return list_freq

def sen_get():
    try: 
        sensors_read = subprocess.getoutput('sensors -u -j -A')
        sensors_read = dict(json.loads(sensors_read))
    except json.JSONDecodeError as Error:
        print(Error)
        sensors_read = None
        exit(-1)
        
    return sensors_read


def get_sensors_data():
    sensors = sen_get()
    sensors_out = []

    value_list = []
    for item, sen in sensors.items():
        for sub_it,data in sen.items():
            for sensor_list, sensor_data in data.items():
                value_list.append(sensor_data)
            sensors_out.append(value_list)
            value_list = []


    return sensors_out


if __name__ == '__main__':
    print(sen_get())
    print(120*'*')
    print(get_sensors_data())
