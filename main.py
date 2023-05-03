"""
from logging import raiseExceptions
import numpy as np
import math as m
from camera import Camera
from shapes import Circle, Donut
from main import Window
from renderer import Renderer
from tkinter import *
__frame_size__ = 100 

if __name__ == "__main__":
    # PROBLEMS WITH ZERO ARRAY IN RENDER()
    #PROBLEM WITH ZERO ARRAY IN RASTERIZATION

    #mat = np.random.randint(10, size = (3, 20))
    #mat = np.array([[4, 4, 4, 4],[4, 4, 4, 4],[3, 8, 7, 1]])
    #mat = np.array([[20, 40, 50],[0, 20, -10],[1, 1, 1]])
    mat = np.array([0, 0, 0])
    #print("The random matrix:")
    #print(mat)
    t = np.zeros(shape = (2, 3))
    par = np.array([[0], [0], [-10]])
    rot = np.array([m.radians(0), m.radians(0), m.radians(0)])
    trans = np.column_stack((par, rot))

    w = Window(60, 60)
    #c = Circle([300])
    c = Donut([300, 100])
    w.update_obj(c.__obj__)
    #print(c.__obj__)
    cam = Camera(w)
    red = Renderer(cam)
    #red.render()

    #red.animate()
    #red.win.mainloop()
    #print(100*"# ")
    #for i in range(100): print("#")

    win = Tk()




    Issue: mode="adjust" weird rotation results especially for 0, 90, 0, see differences between mode = adjust + center
    Issue: centering fucking sucks B) - SOLVED

    """

import engine as e
import gui as g

if __name__ == "__main__":
    w = e.Window(60,60)
    c = e.Donut([300, 100])
    #c = e.Sphere([300])
    w.update_obj(c.__obj__)
    g = g.GUI(w)
    #g.donut()


    """
    settings:
	Window - resolution
	res lock - on/off?
	dark theme - meme
	
graphics:
	frame_size - 
	window_size - make cap depending on res???
	camera settings on/off:
		adjust
		center
		z-depth
	"""
