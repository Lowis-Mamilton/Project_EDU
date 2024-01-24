#導入所需Library
import sensor, image, time
#from pyb import UART  #Send data to element through UART

#相機初始化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_whitebal(False)   #關閉自動白平衡
sensor.set_hmirror(True)  #畫面水平翻轉
sensor.set_vflip(True)   #畫面垂直翻轉
#uart = UART(3, 115200)  #UART setting

threshold   = (20, 58, -48, -9, 11, 27)   #目標顏色閥值

while(True):
    img = sensor.snapshot()

    blobs = img.find_blobs([threshold], pixels_threshold=200, area_threshold=300)

    cX = 0
    cY = 0
    if blobs:
        for b in blobs:
            cX = b.cx()
            cY = b.cy()
            img.draw_rectangle(b.rect())
    print(cX, cY)
    img.draw_cross(cX, cY)
    #uart.write(str(cX) + ',' + str(cY) + '\n')  #Send data