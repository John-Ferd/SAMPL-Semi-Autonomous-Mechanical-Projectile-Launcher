import serial
import time
from helper import normalize_to_servo_range


USB_PORT = "/dev/cu.usbmodem1101";
arduino = serial.Serial(port=USB_PORT,   baudrate=460800, timeout=.1);


def position_servos(servo_power):
    print(f"WROTE {servo_power}")
    arduino.write(str(servo_power).encode())
    read()

def fire():
    #arduino.flush()
    arduino.write(("fire a").encode())
    print("fire")


def read():
    if arduino.isOpen():
        input_data=arduino.readline().strip().decode("utf-8")
        if input_data:
            print("arduino_message")
            print(input_data)