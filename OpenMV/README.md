# OpenMV

* Setup
* ROI 感興趣區域
* UART Communication UART通信
* [Example Code](../OpenMV/Code)


## Setup

* Flowchart
```mermaid
graph LR
A(Download IDE) --> B(Connect to Cam)
B --> C(Test)
C --> |Y| D[Finish]
```
* [OpenMV Website](https://openmv.io/)
* `Step1` :Install OpenMV IDE, visit OpenMV official website, download and install IDE.
* `Step2` :Use cable connect camera to computor.
* `Step3` :Run simple code within the camera.

## ROI 感興趣區域

## UART Communication UART通信
* Put "[matrix_mini.py](../OpenMV/Code/matrix_mini.py)" in the camera.
* Matrix Mini example code. [check here](../OpenMV/Code/MARC.ino)
* If you want to use OpenMV cam to send data to Matrix Mini, you should move the [`SmartCamReader.cpp`](../OpenMV/Code/SmartCamReader.cpp) and [`SmartCamReader.h`](../OpenMV/Code/SmartCamReader.h) to your Arduino program files folder together, you can use this code.

```
#include "SmartCamReader.h"

unsigned int data[20];
float SmartCamReader(data);

color = data[0]; // 1 = red, 2 = blue
cX = data[1]; // Centre X coordinate of the blob
cY = data[2]; // Centre Y coordinate of the blob
Area = data[3]; // Area of the blob
```