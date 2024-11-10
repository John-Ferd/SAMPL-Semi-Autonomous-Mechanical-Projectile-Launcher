#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
#define SERVO1MIN  150 // This is the 'minimum' pulse length count (out of 4096)
#define SERVO1MAX  600 // This is the 'maximum' pulse length count (out of 4096)
#define SERVO_FREQ 60 // Analog servos run at ~50 Hz updates


void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates

  delay(10);
}

void loop() {
  // Drive each servo one at a time using setPWM()

  // pwm.setPWM(SERVO_NUMBER, 0, FREQUENCY)
  if (Serial.available() > 0) {
    String input_str1 = Serial.readStringUntil(' ');
    int input1 = input_str1.toInt();
    //unsigned char _ = Serial.read();
    String input_str2 = Serial.readString();
    int input2 = input_str2.toInt();
    pwm.setPWM(0, 0, input1);
    pwm.setPWM(1, 0, input2);

  }
}
