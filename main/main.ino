#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
#define SERVO1MIN  90 // This is the 'minimum' pulse length count (out of 4096)
#define SERVO1MAX  510 // This is the 'maximum' pulse length count (out of 4096)
#define USMIN  600 // This is the rounded 'minimum' microsecond length based on the minimum pulse of 150
#define USMAX  2400 // This is the rounded 'maximum' microsecond length based on the maximum pulse of 600
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates


void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates

  delay(10);
}

int i=300;
void loop() {
  // Drive each servo one at a time using setPWM()

  // pwm.setPWM(SERVO_NUMBER, 0, FREQUENCY)

  if (Serial.available() > 0) {
    char input = Serial.read();

    if (input == 'a') {
      i -= 10;
      if (i < SERVO1MIN) {
        i = SERVO1MIN;
      }
    } else if (input == 'd') {
      i += 10;
      if (i > SERVO1MAX) {
        i = SERVO1MAX;
      }
    }
    Serial.println(i);
    pwm.setPWM(0, 0, i);
  }
}
