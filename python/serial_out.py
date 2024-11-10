import serial
import time
from helper import normalize_to_servo_range


USB_PORT = "/dev/cu.usbmodem1101";
arduino = serial.Serial(port=USB_PORT,   baudrate=460800, timeout=.1);


def position_servos(servo_power):
    print(f"WROTE {servo_power}")
    arduino.write(str(servo_power).encode());
    #arduino.read(); # UNCOMMENT THIS LINE TO IMPROVE SPACE BAR, BUT REDUCE PERFORMANCE

def fire():
    arduino.write("fire a".encode())