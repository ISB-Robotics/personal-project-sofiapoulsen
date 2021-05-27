//https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing/all

char val; // Data received from the serial port
int ledPin = 13; //pin 13 is the on-board LED

void setup() {
  pinMode(ledPin, OUTPUT); // not sure what this means, oh well
  Serial.begin(9600);
  //Serial: used for communication between the Arduino board and a computer
}

void loop() {
  if (Serial.available()) {
    val = Serial.read(); // store & read the data, if it's available
  }
  if (val == '1') {
    digitalWrite(ledPin, HIGH); // turn the LED on
  } else {
    digitalWrite(ledPin, LOW); // turn it off
  }
  delay(10); 
}
