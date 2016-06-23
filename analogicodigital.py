# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:21:19 2016

@author: Arturo
"""
import mraa # pueda leer los conversores A-D
import time

try:
    pinSensor = mraa.Aio(0)
    pinSensor.setBit(12)  #12 bits 
    while True:
        valorSensor = pinSensor.read()
        print '%.6f '%(valorSensor/819.0)
        time.sleep(1)
except:
	print 'Seguro que tienes un AIX?'
