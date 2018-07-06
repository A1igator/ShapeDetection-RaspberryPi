#!/usr/bin/env python


from picamera import PiCamera
from time import sleep
import serial

camera = PiCamera()   
camera.start_preview()
sleep(5)
camera.capture('/home/pi/shape-detection/shapes_and_colors.png')
camera.stop_preview()
import detect_shapes
