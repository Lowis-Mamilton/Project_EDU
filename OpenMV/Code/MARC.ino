#include "SmartCamReader.h"
#include <MatrixMini.h>

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

    if (color == 1 | color == 2){
      error = (cX - 160)*0.5;
      Mini.M1.set(-50 - error);
      Mini.M2.set(50 - error);
    } else {
      Mini.RGB1.setRGB(0, 255, 0 );
      Mini.M1.set(0);
      Mini.M2.set(0);
    }
  }
}
