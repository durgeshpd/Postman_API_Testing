import serial
import time

ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate = 115200
ser.timeout = 1

while True:
    try:
        ser.open()
        with open('log.txt', 'a') as f:
            while True:
                data = ser.readline()
                f.write(data.decode('utf-8'))
                print(data)
    except serial.SerialException:
        time.sleep(0.01)
    except:
        time.sleep(0.01)
    finally:
        ser.close()
        time.sleep(0.01)
