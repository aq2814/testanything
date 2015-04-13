'''
Created on 2014. 12. 9.

@author: D2954_IPHONE5S
'''

"""
import serial
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate('Some Application Title')

baudrate = 9600

ser = serial.Serial(7)

#print ser.name
ser.baudrate = 9600
while 0 < 1:
    txt = ser.read()
    #print txt
    shell.SendKeys(txt)"""

import serial
import time
from SendKeys import SendKeys as sk

ser = serial.Serial(7)
ser.baudrate = 9600
while 0 < 1:
    txt = ser.read()
    sk(txt, 0)
    #time.sleep(0.1)

    
    