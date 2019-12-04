#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import serial
import time

ser = serial.Serial('/dev/ttyUSB0', timeout=0.2)
if ser.is_open:
    ser.write(b'SYSTem:REMote\r\n')     

with open('./test.log', 'a+') as f:
    while true:
        ser.write(b'MEAS:CURR?\r\n')
        data = ser.readline()
        f.write(str(time.strftime('%Y-%m-%d %H:%M:%S')) + ' ' + str(data) + '\n')
        time.sleep(1)
