# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:49:11 2022

@author: diego
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image, ImageOps
import numpy as np

from matplotlib import pyplot as plt
import matplotlib.image as mpimg

direct = ("C:/Users/diego/Desktop/Filtros/panda.jpg")
plt.imshow(Image.open(direct))



import numpy as np
import colorsys

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def colorize(image, hue):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')

    return new_img

si = colorize(Image.open(direct), 267.9778967)
plt.imshow(si)