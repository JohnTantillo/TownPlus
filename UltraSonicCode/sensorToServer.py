import serial
import requests

nonMagicNumber = 100
count = 0

ser = serial.Serial(
baudrate = 9600,
port = '/dev/ttyACM0'
)


running = True
while running:
    data = ser.readline()
    data = data.rstrip()
    if data != "Out of range":
        if float(data) <= nonMagicNumber:
            count = count + 1
            if count >= 15:
                count = 0
                print("sending to server")
                r = requests.post("/sensorData", data = {'dist':float(dist)})
        else:
            count = 0
#TODO: only send when there is a consistent change
