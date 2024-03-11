#include "SmartCamReader.h"
#include "MatrixMini.h"

unsigned int data[20];
unsigned int color, cX, cY, Area;
unsigned int old_color;

void setup() {
  Mini.begin();
  Serial.begin(115200);  
  Mini.RGB1.setRGB(0, 255, 0 );
  Mini.M1.set(0);
  Mini.M2.set(0);
}

int error;

void loop() {

  float result = SmartCamReader(data);


  if (result > 0){
    color = data[0]; // 1 = red, 2 = blue
    cX = data[1];
    cY = data[2];
    Area = data[3];

    Serial.print("Color:");
    Serial.print(color);
    Serial.print(", X:");
    Serial.print(cX);
    Serial.print(", Y:");
    Serial.print(cY);
    Serial.print(", Area:");
    Serial.print(Area);

  }
}
