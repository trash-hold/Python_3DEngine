from lib.tkinter_lib import *


class Menu(tk.Frame):
    '''
    Menu class handles main menu and settings frame
    '''
    def __init__(self, gui):
        tk.Frame.__init__(self, gui.root)
        self.gui = gui
        self.root = gui.root

        self.menu_frame()

        #Calls for resize everytime user changes window size
        self.bind("<Configure>", self.resize)

    def menu_frame(self) -> None:
        '''
        Initializes menu frame
        '''
        #Setting up the geometry of frame
        self.reset()
        tk.Grid.rowconfigure(self, 0, weight = 4, minsize = 40)
        tk.Grid.rowconfigure(self, (1,2,3,4), weight = 1, minsize = 10)
        tk.Grid.rowconfigure(self, 5, weight = 1, minsize = 30)
        tk.Grid.columnconfigure(self, 1, weight = 1, minsize = 80)
        tk.Grid.columnconfigure(self, (0, 2), weight = 1, minsize = 50)

        #Creating buttons and labels          
        l1 = s.MenuLabel(self, text = s.menu_banner)
        b1 = s.MenuButton(self, text = "Spin me!", command=lambda: self.gui.change_frame('Animation'))
        b2 = s.MenuButton(self, text = "Freemode", command=lambda: self.gui.change_frame('Freemode'))
        b3 = s.MenuButton(self, text = "Settings", command = self.settings_frame)
        b4 = s.MenuButton(self, text = "Exit", command = self.close_win)

        #Helper lists
        buttons = [b1, b2, b3, b4]
        self.widgets = [l1, b1, b2, b3, b4]

        #Packing the label
        l1.grid(row = 0, column = 0, sticky = "NSWE", pady = (0, 80), columnspan = 3)
        
        #Packing buttons into grid
        counter = 1
        for i in buttons:
            i.grid(row = counter, column = 1, sticky = "NSWE", pady = 10)
            counter += 1


    def settings_frame(self) -> None:
        '''
        Initializes settings frame
        '''
        self.reset()

        #Creating frames
        top_frame = tk.Frame(self)
        self.sett_frame = tk.Frame(self)

        #Creating top_frame widgets
        sett = s.BigLabel(top_frame, text = "Settings")
        sett.configure(bg = s.main_theme, fg = s.background_theme, pady = 10)
        exit = s.MenuButton(top_frame, text = "<")
        exit.configure(relief = tk.FLAT, padx = 20, command = self.menu_frame)

        #Packing top_frame
        exit.pack(side = tk.LEFT, padx = (0, 10), fill = tk.Y)
        sett.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

        #Creating settings_frame widgets
        f_size = s.ValueSetting(master = self.sett_frame, label = "Frame size", entry = "60")
        w_size = s.ValueSetting(master = self.sett_frame, label = "Window size", entry = "60")
        tick = s.ValueSetting(master = self.sett_frame, label = "Tick duration", entry = "25", _min = 10, _max = 50)
        adjust_butt = s.OFButton("Camera adjust", True, master = self.sett_frame)
        center_butt = s.OFButton("Center", True, master = self.sett_frame)
        zdepth_butt = s.OFButton("Z-depth reduction", False, master = self.sett_frame)

        #Packing settings_frame 
        f_size.pack(fill = tk.X, pady = 10)
        w_size.pack(fill = tk.X, pady = 10)
        tick.pack(fill = tk.X, pady = 10)
        adjust_butt.pack(fill = tk.X, pady = 10)
        center_butt.pack(fill = tk.X, pady = 10)
        zdepth_butt.pack(fill = tk.X, pady = 10)
        
        #Packing into main frame
        top_frame.pack(side = tk.TOP, fill = tk.X)
        self.sett_frame.pack(fill = tk.Y, pady = 20, expand = False)

    def resize(self, event) -> None:
        '''
        Handles resize operation when user changed window size
        '''
        new_x = self.root.winfo_width() 
        new_y = self.root.winfo_height()
        
        self.frame_resize(self, [new_x, new_y])
            

    def frame_resize(self, frame: tk.Frame, delta: list()) -> None:
        '''
        Changes sizes of every button/label
        '''
        i_info = None
        for i in frame.winfo_children():
            if isinstance(i, (tk.Frame, s.OFButton, s.ValueSetting)): 
                self.frame_resize(i, delta)
            else: 
                i_info = i.cget('font').split(" ")
                if isinstance(i, s.MenuLabel): 
                    new_label = s.resize_info(i_info[0], delta[0])
                else:
                    new_label = s.resize_info(i_info[0], delta[1], True)
                i.configure(font = new_label)

    def reset(self) -> None:
        '''
        Cleans up frame
        '''
        self.configure(bg = s.background_theme)
        for widget in self.winfo_children():
            widget.destroy()
        
    def close_win(self):
        self.root.destroy()
