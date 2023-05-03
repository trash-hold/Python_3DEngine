from os import rename
import tkinter as tk
from time import sleep

from engine import *
from gui.menu import Menu
from gui.animation import Animation
import gui.styles as s

"""
Functions of GUI:
    - handling frames -> updating window when they change
    - controlling app flow -> destroying frames that won't be needed
    - configuring window size and properties
    - communicating with the engine
"""


class GUI:
    def __init__(self, window):
        #Setting up engine
        self.win = window
        self.cam = Camera(window)
        self.ren = Renderer(self.cam)

        #Initializing TK
        self.root = tk.Tk()

        #Default GUI settings
        self.root.geometry("1080x720")
        self.root.minsize(480, 640)
        self.root.tk_setPalette(
            background = s.background_theme, 
            foreground = s.main_theme
        )
        self.root.option_add("*Font", "Terminal")
        self.root.wm_attributes("-transparentcolor", s.trans )

        #Packing main menu frame on init
        self.frames = []
        self.frames.append(Menu(self))
        self.frames[0].pack(fill = tk.BOTH, expand = True)

        #self.root.bind('<Configure>', self.update_res)

        self.root.mainloop()

    def return_menu(self) -> None:
        self.reset_frame()
        self.frames.pop()
        self.frames.append(Menu(self))
        self.frames[-1].pack(fill = tk.BOTH, expand = True)

    def animation_frame(self) -> None:
        self.reset_frame()
        self.frames.pop()
        self.frames.append(Animation(self))
        self.frames[-1].pack(fill = tk.BOTH, expand = True)

    def donut(self):
        '''
        Pre-programmed rotation sequence
        '''
        self.reset_frame()
        top_frame = tk.Frame(self.root)

        #Initial render from engine
        self.ren.render()
        self.counter = 0

        #Creating top_frame widgets
        sett = s.BigLabel(top_frame, text = "Animation")
        sett.configure(bg = s.main_theme, fg = s.background_theme, pady = 10)
        exit = s.MenuButton(top_frame, text = "<")
        exit.configure(relief = tk.FLAT, padx = 20, command = self.return_menu)

        #Packing top_frame
        exit.pack(side = tk.LEFT, padx = (0, 10), fill = tk.Y)
        sett.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

        self.object_img = s.DisplayLabel(self.root, text = "", width = int(self.win.__wsize__[0]*1.5), height =  int(self.win.__wsize__[1]*2))
        #self.object_img = tk.Label(self.root, text = "", width = int(self.win.__wsize__[0]*1.5), height =  int(self.win.__wsize__[1]*2), font = "TkFixedFont", justify = tk.CENTER)

        #self.start_butt.pack()
        top_frame.pack(side = tk.TOP, fill = tk.X)
        self.object_img.pack(fill = tk.NONE, pady = 20, padx = 30, expand = True)

        self.animation()
        self.root.mainloop()
    
    """def update_img(self):
        sleep(self.ren.__refresh_rate__)
        self.image = self.ren.__image__
        if self.counter < 360: 
            if self.counter == 0: self.start_var.set("")
            self.start_butt.invoke()
        self.counter = self.counter + 1"""

    def animation(self):
        ren = self.ren
        cam = self.cam
        if self.counter < 360:
            ren.render()
            self.object_img.config(text = ren.__image__)
            cam.cam_reset()
            cam.rotate([0, -180 + self.counter, -180 + self.counter], True)
            self.counter += 1
            self.root.after(25, self.animation)

    def reset_frame(self):
        self.root.configure(bg = s.background_theme)
        for widget in self.root.winfo_children():
            widget.destroy()

"""class FrameHandler(tk.Frame):
    def __init__(self, gui):
        self.gui = gui
        self.frames = []
        tk.Frame.__init__(self.gui.root)"""

