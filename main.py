import os
import threading
import time
import sys
from threading import Thread
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
from xmlrpc.client import DateTime
import shutil

#from uartrisc import RISCV_COM
#from uartardu import Arduino_COM
from webscrape import Get_Prices
from updater import Update

def RiscInt():
    while True:
        print("Risc")
        time.sleep(10)

def ArduInt():
    while True:
        print("Ardu")
        time.sleep(5)

GotPrices = 0
Updated = 0
UpHour = 0
UartInterval = 0

print("Starting uart interval threads...")
t1 = threading.Thread(target=RiscInt)
t2 = threading.Thread(target=ArduInt)
t1.daemon = True
t2.daemon = True
t1.start()
t2.start()
time.sleep(1)

while True:
    DT = datetime.now()

    DT = str(DT)

    year = int(DT[:4])
    month = int(DT[5:7])
    day = int(DT[8:10])

    hour = int(DT[11:13])
    minutes = int(DT[14:16])
    seconds = int(DT[17:19])

    if hour == 15 and GotPrices == 0:
        Update()
        Get_Prices()
        GotPrices = 1
    if hour == 16 and GotPrices == 1:
        GotPrices = 0

    if Updated == 0:
        print("Running updater..")
        Update()
        Updated = 1
        UpHour = hour
    if hour == (UpHour+1):
        Updated = 0
    
    CTime = time.time()
    




    


    


