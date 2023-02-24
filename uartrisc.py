import serial
import RPi.GPIO as GPIO
from time import sleep             # lets us have a delay
import fileinput
import os

def RISCV_COM():
    GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
    GPIO.setup(18, GPIO.OUT)           # set GPIO24 as an output
    ser = serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1.0)
    
    Data = "S"
    
    f = open('States.txt', 'r')
    while True:
        line = f.readline()
        L = len(line)
        L = L-1
        if not line:
            break
        if "Power" in line:
            Data = Data+line[6:7]
        if "PriceNow" in line:
            Data = Data+"P"+line[len("PriceNow="):L]
        if "Consumption" in line:
            Data = Data+"C"+line[len("Consumption="):L]
        if "WaterTemp" in line:
            Data = Data+"T"+line[len("WaterTemp="):L]
        if "Expense" in line:
            Data = Data+"E"+line[len("Expense="):L]
    
    
    
    Data = Data+"X"

    print("Sending " + Data + " to RiscV..")

    GPIO.output(18,1)
    sleep(1)
    
    ser.write(bytes(Data,"iso-8859-1"))
    
    GPIO.output(18,0)
    sleep(1)
    
    f.close()
    
    f2 = open('temp.txt', 'a')
    f = open('States.txt', 'r')
    
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
                break;
    Datar = Datar[1:]
    Datar = Datar[:-1]
    print (Datar)

    print("(" + Datar ") Recieved from RiscV")
    
    while True:
        line = f.readline()
        if not line:
            break
        if "AirTemp" in line:
            f2.write("AirTemp="+Datar+"\n")
        else:
            f2.write(line)
    
    
    f2.close()
    f.close()
    
    os.remove("States.txt")
    os.rename("temp.txt", "States.txt")
    
    GPIO.cleanup()






    


