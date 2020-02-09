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
    data = str(ser.readline())
    #data = data[2:]
    # data = data.strip("\n\r")
    # if data != "Out of range":
    #     if float(data) <= nonMagicNumber:
    #         count = count + 1
    #         if count >= 15:
    #             count = 0
    #             print("sending to server")
    #     else:
    #         count = 0
    print(data)
#TODO: only send when there is a consistent change
