#include<Servo.h>

Servo servoMotor;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  servoMotor.attach(9);
}

void loop() {
  if ( Serial.available() > 0 ) {
    char option = Serial.read();
    if (option == '1'){
      servoMotor.write(0);
    }
    else if (option == '2'){
      servoMotor.write(180); 
    }
      
    }
  }
