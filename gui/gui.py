from os import rename
import tkinter as tk
from time import sleep

from engine import *
from gui.menu import Menu
from gui.animation import Animation
from gui.freemode import Freemode
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
        self.cam = Camera(self.win)
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
        #self.change_frame('Menu')
        self.change_frame('Freemode')

        #self.root.bind('<Configure>', self.update_res)

        self.root.mainloop()
    
    def change_frame(self, frame_name):
        frames = {
            'Menu': Menu,
            'Animation': Animation,
            'Freemode': Freemode
        }
        self.reset_frame()
        frame_class = frames[frame_name]

        new_frame = frame_class(self)
        new_frame.pack(fill = tk.BOTH, expand = True)

    def reset_frame(self):
        self.root.configure(bg = s.background_theme)
        for widget in self.root.winfo_children():
            widget.destroy()
