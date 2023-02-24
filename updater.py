import time
import os
from datetime import date
from datetime import datetime
from datetime import timedelta
import fileinput
from xmlrpc.client import DateTime
import shutil

def Update():
    DT = datetime.now()

    DT = str(DT)

    year = int(DT[:4])
    month = int(DT[5:7])
    day = int(DT[8:10])

    hour = int(DT[11:13])
    minutes = int(DT[14:16])

    f = open("PriceZones/Tomarrow/SE3/PriceTable.txt", 'r')

    PriceDate = f.readline()

    f.close()

    PDyear = int(PriceDate[6:])
    PDmonth = int(PriceDate[3:5])
    PDday = int(PriceDate[:2])

    today = date.today()

    if today == date(PDyear, PDmonth, PDday):
        print("Prices for today loaded succesfully!")
        if os.path.exists("PriceZones/SE1"):
            shutil.rmtree("PriceZones/SE1")
            shutil.rmtree("PriceZones/SE2")
            shutil.rmtree("PriceZones/SE3")
            shutil.rmtree("PriceZones/SE4")
        if os.path.exists("PriceZones/Tomarrow/SE1"):
            shutil.copytree("PriceZones/Tomarrow/SE1", "PriceZones/SE1")
            shutil.copytree("PriceZones/Tomarrow/SE2", "PriceZones/SE2")
            shutil.copytree("PriceZones/Tomarrow/SE3", "PriceZones/SE3")
            shutil.copytree("PriceZones/Tomarrow/SE4", "PriceZones/SE4")

        f = open("PriceZones/SE3/PriceTable.txt", 'r')
        while True:
            line = f.readline()
            if not line:
                break
            if int(line[:2]) == hour:
                PriceNow = line[3:line.find(',')]

        f1 = open('temp.txt', 'a')
        f2 = open('States.txt', 'r')

        while True:
            line = f2.readline()
            if not line:
                break
            if "PriceNow" in line:
                f1.write("PriceNow="+PriceNow+"\n")
            else:
                f1.write(line)

        f1.close()
        f2.close()

        os.remove("States.txt")
        os.rename("temp.txt", "States.txt")

        f.close()
    else:
        print("Error: Prices Date not today!")
        if os.path.exists("PriceZones/SE1"):
            shutil.rmtree("PriceZones/SE1")
            shutil.rmtree("PriceZones/SE2")
            shutil.rmtree("PriceZones/SE3")
            shutil.rmtree("PriceZones/SE4")

        f = open('States.txt', 'r')
        f2 = open('temp.txt', 'a')

        while True:
            line = f.readline()
            if not line:
                break
            if "Power" in line:
                f2.write("Power="+'0'+"\n")
            else:
                f2.write(line)
    







        
        