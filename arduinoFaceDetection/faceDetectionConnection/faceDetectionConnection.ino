//using https://www.learnrobotics.org/blog/face-tracking-opencv/
#include <Servo.h>
Servo servo;

String readString;

int servoX = 0 ;
// ^ this is the minimum amount the 
// difference in positions sent has to be,
// to prevent the eye from just oscillating like crazy. 
int prevPos = 10;

const int minPos = 70; 
const int maxPos = 128;

const int minDif = 10;
void setup() {
  servo.attach(7); 
  Serial.begin(9600);
  
}


void loop() {
  if(Serial.available()) { 
     int input = Serial.parseInt(); //read & store any incoming integers 
     if (input > 0) {
      
        servoX = map(input, 200, 1700, maxPos, minPos); 
        if ((servoX - prevPos) > minDif) {
          
          Serial.println(servoX);
          //^^ change the range of x coordinates from the width of the video captured (200-1500)
          // to the rotation of the servo (0-170). 
          servo.write(servoX); //move the servo by the amount entered
           
        } else {
          delay(50);
        }
     } 
  } 
  delay(100);

}

//b'1166\r\n'
