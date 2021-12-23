from tkinter import *
from PIL import ImageGrab
import screen_brightness_control as sbc

import cv2
import numpy
import time

threshold = 125

def color_detect():
    
  
 
 while True:
        avg_img = ImageGrab.grab()
        avg_color_per_row = numpy.average(avg_img, axis=0)
        avg_color = numpy.average(avg_color_per_row, axis=0)


        if avg_color[0] > threshold:
            sbc.fade_brightness(20, interval=0.001, increment=15)
            print("Highter")
            continue

        if avg_color[1] > threshold:
            sbc.fade_brightness(20, interval=0.001, increment=15)
            print("Highter")
            continue
            
        if avg_color[2] > threshold:
            sbc.fade_brightness(20, interval=0.001, increment=15)
            print("Highter")
            continue

        if avg_color[0] < threshold:
            sbc.fade_brightness(90, interval=0.001, increment=15)
            print("Highter")
            continue

        if avg_color[1] < threshold:
            sbc.fade_brightness(90, interval=0.001, increment=15)
            print("Highter")
            continue
            
        if avg_color[2] < threshold:
            sbc.fade_brightness(90, interval=0.001, increment=15)
            print("Highter")
            continue
            

        # if avg_color[0] < threshold:
        #         print("Continue")
        #         continue

        # if avg_color[1] < threshold:
        #         print("Continue")
        #         continue
                

        # if avg_color[2] < threshold:
        #         print("Continue")
        #         continue


 
            

