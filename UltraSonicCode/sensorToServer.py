import serial

ser = serial.Serial(
baudrate = 9600,
port = '/dev/ttyACM0'
)


running = True
while running:
    data = ser.readline()
    data = data.rstrip()
    stringData = str(data)
    print(stringData)
#TODO: only send when there is a consistent change
