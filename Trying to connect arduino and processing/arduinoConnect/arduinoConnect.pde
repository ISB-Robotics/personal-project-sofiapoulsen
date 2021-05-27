//https://learn.sparkfun.com/tutorials/connecting-arduino-to-processing/all
import processing.serial.*;

Serial myPort; // Create object from Serial class
String val;   // Data received from the serial port

void setup() { 
  
  size(200, 200); // make the canvas 200 by 200 px big
  
  String portName = Serial.list()[1]; //change the [] to match the port, 
  //[1] seems to work for the USB port 

  myPort = new Serial(this, portName, 9600);
  // ^set up our Serial object to listen to the port Arduino is connected to 
  //9600 is the speed, make sure it's the same as Arduino's Serial.Begin(9600)
}

void draw() { // = void loop()
  // RECIEVE FROM ARDUINO: 
  /*
  if ( myPort.available() > 0) {
    val = myPort.readStringUntil('\n');
  }
  println(val);
  */
  // SEND TO ARDUINO: 
  if (mousePressed) {
    myPort.write('1');
    println("1");
  } else {
    myPort.write('0');
  }
}
