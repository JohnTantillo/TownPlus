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
    print(data, flush=True)
    if data != "Out of range":
        count2 = 0
        count = count + 1
        if count >= 200:
            count = 0
            print("sending to server")
            r = requests.post("http://165.227.223.64/sensorData", data = {'dist':float(data)})
    else:
        count = 0
        count2 = count2 + 1
        if count2 >= 200:
            count2 = 0
            r = requests.post("http://165.227.223.64/sensorData", data = {'dist':-1})
#TODO: only send when there is a consistent change
