
from tkinter import *
from PIL import ImageGrab
import screen_brightness_control as sbc
from color_detect import color_detect as COLOR

import cv2
import numpy
import time




root = Tk()
root.title('Screen Brightness Auto-Adjuster')
root.geometry("400x100")


userButton = Button(root, command=COLOR, text="Click", state=ACTIVE)
userButton.pack()

exitButton = Button(root, command=exit, text="Exit", state=ACTIVE)
exitButton.pack(pady=20)


               
root.mainloop()
exit(0)





# image = ImageGrab.grab()
# for y in range(0, 100, 10):
#     for x in range(0, 100, 10):
#         color = image.getpixel((x, y))

# average = image.mean(axis=0).mean(axis=0)

# pixels = np.float32(image.reshape(-1, 3))

# n_colors = 5
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
# flags = cv2.KMEANS_RANDOM_CENTERS

# _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
# _, counts = np.unique(labels, return_counts=True)

