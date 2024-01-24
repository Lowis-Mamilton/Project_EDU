/*
    This is Matrix Mini and OpenMV UART sample code.

    Made by Barry.
    Date: Wed, 24, Jan.
*/

#include "MatrixMini.h"

void setup() {
  Mini.begin();
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int pos = data.indexOf(',');
    String value1_str = data.substring(0, pos);
    String value2_str = data.substring(pos + 1);
      
    int cX = value1_str.toInt();
    int cY = value2_str.toInt();
  
    Serial.print("cX: ");
    Serial.print(cX);
    Serial.print(", cY: ");
    Serial.println(cY);
  }
}

