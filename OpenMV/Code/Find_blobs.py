'''
    This is Matrix Mini and OpenMV UART sample code.

    Date: Wed, 24, Jan.
'''

import sensor, image, time
from matrix_mini import send_data

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_auto_whitebal(False)
sensor.skip_frames(time = 1000)

sensor.set_vflip(True)
sensor.set_hmirror(True)

red_threshold = (0, 100, -128, 127, -128, 127)
blue_threshold = (0, 100, -128, 127, -128, 127)

clock = time.clock()
while(True):
    clock.tick()
    img = sensor.snapshot()

    r_blob_area = 0
    bl_blob_area = 0


    red_blobs = img.find_blobs([red_threshold], pixels_threshold=300, area_threshold=550)
    blue_blobs = img.find_blobs([blue_threshold], pixels_threshold=300, area_threshold=550)
    if red_blobs:
        max_r_blob = max(red_blobs, key=lambda b: b[2]*b[3])
        r_blob_area = round(max_r_blob.area()/2)

    if blue_blobs:
        max_bl_blob = max(blue_blobs, key=lambda b: b[2]*b[3])
        bl_blob_area = round(max_bl_blob.area()/2)

    color = 0
    x_center = 0
    y_center = 0
    blob_area = 0

    #detect colour and export
    if r_blob_area > 0 or bl_blob_area > 0:
        if r_blob_area > bl_blob_area:
            color = 1
            blob_area = r_blob_area
            max_blob = max_r_blob
        else :
            color = 2
            blob_area = bl_blob_area
            max_blob = max_bl_blob

        #draw a rectangle
        img.draw_rectangle(max_blob.rect())

        x_center = max_blob.cx() #max=320
        y_center = max_blob.cy() #max=240

        #draw a cross
        img.draw_cross(x_center, y_center)

        #show coordinates
        #img.draw_string(0, 0, str(x_center) + ", " + str(y_center))

    #export the data to matrix mini
    send_data([color, x_center, y_center, blob_area])
    #print(clock.fps()) #show cam fps
