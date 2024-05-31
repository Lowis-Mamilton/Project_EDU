# [OpenMV](https://openmv.io/)

* [Setup 前置設定](../OpenMV/README.md#setup-前置設定)
* [Initialization 初始化](../OpenMV/README.md#initialization-初始化)
* [ROI 感興趣區域](../OpenMV/README.md#roi-感興趣區域)
* [UART Communication UART通信](../OpenMV/README.md#uart-communication-uart通信)
* [Example Code](../OpenMV/Code)
* [Learn more](https://book.openmv.cc/)


## Setup 前置設定

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

## Initialization 初始化
```
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA) # 320*180
sensor.skip_frames(time = 2000) # Delay

#Turn off automatic white balance
sensor.set_auto_whitebal(False)

#Flip the frame horizontally
sensor.set_hmirror(True)

#Flip the frame vertically
sensor.set_vflip(True)
```


## ROI 感興趣區域
A region of interest (often abbreviated ROI) is a sample within a data set identified for a particular purpose. The concept of an ROI is commonly used in many application areas. For example, in medical imaging, the boundaries of a tumor may be defined on an image or in a volume, for the purpose of measuring its size.


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

