# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:19:41 2016

@author: Arturo
"""
import mraa 
import time

led = mraa.Gpio(13)
pin2 = mraa.Gpio(2)
pin4 = mraa.Gpio(4)
pin2.dir(mraa.DIR_IN)
pin4.dir(mraa.DIR_IN)
led.dir(mraa.DIR_OUT)
entrada1 = 0 
entrada2 = 0 
salida = 0

while True:
    entrada1 = pin2.read()
    entrada2 = pin4.read()
    salida = entrada1 & entrada2
    print salida
    led.write(salida)
    time.sleep(1)