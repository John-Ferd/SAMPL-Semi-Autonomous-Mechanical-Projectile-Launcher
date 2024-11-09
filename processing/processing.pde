

import processing.serial.*;
Serial port;

String USB_PORT = "/dev/cu.usbmodem1101"; // Set this to appropriate value on local system
void setup() {
  port = new Serial(this, USB_PORT, 9600);
}

void draw() {
  
}

void keyPressed() {
  if (key == 'a') {
    port.write("a");
  } else if (key == 'd') {
    port.write("d");
  }
}
