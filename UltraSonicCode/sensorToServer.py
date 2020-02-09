import serial
import requests
import ssl

nonMagicNumber = 100
count = 0
count2 = 0

ser = serial.Serial(
baudrate = 9600,
port = '/dev/ttyACM0'
)


running = True
while running:
    data = str(ser.readline())
    data = data[2:]
    data = data.replace("\\r\\n", "")
    data = data.replace("\'", "")
    #print(data, flush=True)
    if data != "Out of range":
        count2 = 0
        count = count + 1
        if count >= 33:
            count = 0
            print("sending " + str(data) + " to server")
            r = requests.post("http://178.128.238.139/sensorData", data = {'dist':float(data)})
    else:
        count = 0
        count2 = count2 + 1
        if count2 >= 33:
            count2 = 0
            print("sending " + str(-1.0) + " to server")
            r = requests.post("http://178.128.238.139/sensorData", data = {'dist':-1.0})
#TODO: only send when there is a consistent change
