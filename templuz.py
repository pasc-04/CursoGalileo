# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:30:23 2016

@author: Arturo
"""
import signal
import sys

import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

def interruptHandler(signal, frame):
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, interruptHandler)

    myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
    sensortemp = grove.GroveTemp(0)
    sensorluz = grove.GroveLight(1)

    colorR = 255;
    colorG = 0;
    colorB = 0;
    myLcd.setColor(colorR,colorG,colorB)
# Read the input and print, waiting 1/2 second between readings
    while True:
         valorSensor= sensorluz.value();
         myLcd.setCursor(0,0)
         myLcd.write('luz %6d'% valorSensor)
         time.sleep(0.5)
         
         valorSensor= sensortemp.value();
         myLcd.setCursor(1,0)
         myLcd.write('tem %6d'% valorSensor)
         time.sleep(0.5)

    del sensortemp

    del sensorluz