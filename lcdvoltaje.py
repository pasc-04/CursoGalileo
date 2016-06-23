# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:56:08 2016

@author: Arturo
"""

import time
import mraa
import pyupm_i2clcd as lcd
#import pyupm_grove as grove

myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

myLcd.setCursor(0,0)
myLcd.setColor(0,0,255)
myLcd.write('Voltaje: ')
#myLcd.setCursor(1,0)

try:
    pinSensor = mraa.Aio(0)
    pinSensor.setBit(12)    
    while True:
        valorsensor = pinSensor.read()
        myLcd.setCursor(1,0)
        myLcd.write("%.6f"%(valorsensor/819.0))
        time.sleep(1)
except:
    print "Seguro que tienes un ADC?"