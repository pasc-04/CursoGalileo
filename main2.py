# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 09:18:32 2016

@author: Arturo
"""

#!/usr/bin/python
import time
import sys
import signal
def manejadorsenial(signal, frame):
    sys.exit(0)
    signal.signal(signal.SIGINT, manejadorsenial)
    while (True):
        print "Hola, desde el curso de Intel Galileo"
        time.sleep(5)
#Fin de archivo