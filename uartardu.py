import serial
import RPi.GPIO as GPIO
import fileinput
import os
from time import sleep   
import math 

def Arduino_COM():
    GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
    GPIO.setup(23, GPIO.OUT)           # set GPIO24 as an output
    ser = serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1.0)

    # Request from arduino 10ms 

    GPIO.output(23,1)
    sleep(0.1)

    Data = "SsX"

    ser.write(bytes(Data,"iso-8859-1"))
    
    Datar = ""
    
    encoding = 'utf-8'
    
    while True:
            recived_data = ser.read()
            sleep(0.03)
            data_left = ser.inWaiting()
            recived_data += ser.read(data_left)
            Datar = Datar+str(recived_data, encoding)
            ser.write(recived_data)
            if "X" in Datar:
                break

    print("Recived from ATMEGA: (" + str(Datar) + ")")

    Datar = Datar[1:]
    Datar = Datar[:-1]
    Power = Datar[3:4]
    WaterTemp = Datar[:2]

    sleep(0.01)
    GPIO.output(23,0)

    #Calculation

    f = open('States.txt', 'r')
    f2 = open('temp.txt', 'a')

    while True:
        line = f.readline()
        if not line:
            break
        if "Power" in line:
            f2.write("Power="+Power+"\n")
        elif "WaterTemp" in line:
            f2.write("WaterTemp="+WaterTemp+"\n")
        else:
            f2.write(line)
        if "PriceNow" in line:
            Price = line.replace("PriceNow=", "")
        if "AirTemp" in line:
            AirTemp = line.replace("AirTemp=", "")

    AirTemp = int(AirTemp)
    Price = int(Price)
    NowTemp = int(WaterTemp)
    WaterTemp = int(WaterTemp)

    f2.close()
    f.close()

    os.remove("States.txt")
    os.rename("temp.txt", "States.txt")

    if AirTemp < 40:
        WaterTemp = (60 * (math.exp(-Price/300))+(Price/30)) + (70 * 0.2 * (1 - (AirTemp/40))  + ((AirTemp*AirTemp)/500))
    if AirTemp > 40:
        WaterTemp = (60 * (math.exp(-Price/300))+(Price/30)) - (70 * 0.1 * ((AirTemp-40)/20)  + ((AirTemp*AirTemp)/500))
    if AirTemp == 40:
        WaterTemp = (60 * (math.exp(-Price/300)) +(Price/30) + ((AirTemp*AirTemp)/500))
    if WaterTemp < 40:
        WaterTemp = 40
    if WaterTemp > 70:
        WaterTemp = 70

    WaterTemp = int(WaterTemp)

    print("Target WaterTemp: " + str(WaterTemp))

    if os.path.exists("PriceZones/SE3"):
        Power = 0
    elif WaterTemp >= NowTemp:
        Power = 1
    else:
        Power = 0

    # Send to arduino

    GPIO.output(23,1)
    sleep(0.1)

    Data = "S"

    f = open('States.txt', 'r')
    while True:
        line = f.readline()
        L = len(line)
        L = L-1
        if not line:
            break
        if "Power" in line:
            Data = Data+str(Power)



    Data = Data+"X"

    ser.write(bytes(Data,"iso-8859-1"))

    sleep(0.01)
    GPIO.output(23,0)

    print("Sent (" + Data + ") to Arduino..")

    f.close()

    GPIO.cleanup()
