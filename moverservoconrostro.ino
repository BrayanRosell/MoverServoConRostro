#include <Servo.h>
Servo myservo;

int pinServo = 9;
void setup() {
  Serial.begin(9600);
  myservo.attach(pinServo);
}

void loop(){


  char caracter = Serial.read();
  if (caracter=='i'){
   myservo.write(0);
  }
  if (caracter=='d'){
   myservo.write(180);//90
  }
 
}
