from engine import *
from lib.tkinter_lib import *
from gui.frames.menu import Menu
from gui.frames.animation import Animation
from gui.frames.freemode import Freemode

class GUI:
    """
    Functions of GUI:
        - handling frames -> switching between frames 
        - configuring app and engine properties
        - communicating with the engine
    """
    def __init__(self, window):
        #Setting up engine
        self.win = window
        self.cam = Camera(self.win)
        self.ren = Renderer(self.cam)

        #Initializing TK
        self.root = tk.Tk()

        #Default GUI settings
        self.root.title('Real Engine')
        self.root.geometry("1080x720")
        self.root.minsize(1280, 800)
        self.root.tk_setPalette(
            background = s.background_theme, 
            foreground = s.main_theme
        )
        self.root.option_add("*Font", "Terminal")
        self.root.wm_attributes("-transparentcolor", s.trans )

        #Packing main menu frame on init
        self.change_frame('Menu')

        self.root.mainloop()
    
    def change_frame(self, frame_name):
        '''
        Loads new frame of frame_name class
        '''
        frames = {
            'Menu': Menu,
            'Animation': Animation,
            'Freemode': Freemode
        }
        
        if frame_name not in frames.keys(): 
            raise NotImplementedError('GUIerr: Tried to load nonexistant frame')

        #Cleaning existing frame
        self.reset_frame()

        #Creating new frame
        frame_class = frames[frame_name]
        new_frame = frame_class(self)

        #Loading new frame
        new_frame.pack(fill = tk.BOTH, expand = True)

    def reset_frame(self):
        '''
        Brings frame to a default state
        '''
        self.root.configure(bg = s.background_theme)
        for widget in self.root.winfo_children():
            widget.destroy()
