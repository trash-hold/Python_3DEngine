from os import rename
import tkinter as tk
from time import sleep

from engine import *
from gui.menu import Menu

"""
Functions of GUI:
    - handling frames -> updating window when they change
    - controlling app flow -> destroying frames that won't be needed
    - configuring window size and properties
    - communicating with the engine
"""


class GUI:
    def __init__(self, window):
        self.win = window
        self.cam = Camera(window)
        self.ren = Renderer(self.cam)

        self.root = tk.Tk()
        self.root.eval('tk::PlaceWindow . center')

        self.root.geometry("1080x720")
        self.root.minsize(480, 640)
        self.root.configure(bg = "#292929")

        self.frames = []
        self.frames.append(Menu(self))

        self.frames[0].pack(fill = tk.BOTH, expand = True, padx = 90, pady = (40,60))

        #self.root.bind('<Configure>', self.update_res)

        self.root.mainloop()

    def re_pack(self):
        pass


    def donut(self):
        self.ren.render()
        print(self.ren.__image__)

        #self.frame.geometry("100x100")
        #frame = tk.Frame
        self.counter = 0
        self.frames[0].destroy()

        self.start_var = tk.StringVar()
        self.start_var.set("Start")
        self.start_butt = tk.Button(self.root, textvariable = "", command = self.animation, bg = "black", fg="black")

        self.image = tk.StringVar()
        self.image.set(self.ren.__image__)
        
        self.b = tk.Button(self.root, text = "", command = self.update_img)
        self.l = tk.Label(self.root, text = "", bg = "black", width = int(self.win.__wsize__[0]*1.5), height =  int(self.win.__wsize__[1]*2), justify = "center", font='TkFixedFont', fg = "white")

        #self.start_butt.pack()
        self.l.pack()

        self.animation()
        self.root.mainloop()
    
    def update_img(self):
        sleep(self.ren.__refresh_rate__)
        self.image = self.ren.__image__
        if self.counter < 360: 
            if self.counter == 0: self.start_var.set("")
            self.start_butt.invoke()
        self.counter = self.counter + 1

    def animation(self):
        ren = self.ren
        cam = self.cam
        if self.counter < 360:
            ren.render()
            self.l.config(text = ren.__image__)
            cam.cam_reset()
            cam.rotate([0, -180 + self.counter, -180 + self.counter], True)
            self.counter += 1
            self.root.after(25, self.animation)



"""class FrameHandler(tk.Frame):
    def __init__(self, gui):
        self.gui = gui
        self.frames = []
        tk.Frame.__init__(self.gui.root)"""

