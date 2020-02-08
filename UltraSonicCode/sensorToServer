import serial
import io

with serial.Serial() as ser:
    ser.baudrate = 9600
    ser.port = 'COM1'
    ser.open()

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

running = True
while running:
    sio.flush()
    data = sio.readline()
    print(data)
