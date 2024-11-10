import serial
from helper import normalize_to_servo_range


USB_PORT = "/dev/cu.usbmodem1101";
arduino = serial.Serial(port=USB_PORT,   baudrate=9600, timeout=.1);


def write(servo_power):
    print(f"WROTE {servo_power}")
    arduino.write(str(servo_power).encode());