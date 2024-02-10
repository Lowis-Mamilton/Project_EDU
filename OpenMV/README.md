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
* If you want to use OpenMV cam send data to Matrix Mini, you can use this code.

```
#include "SmartCamReader.h"
float SmartCamReader(data);
```