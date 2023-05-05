from lib.tkinter_lib import *

'''
Menu class handles main menu and settings frame
'''
class Menu(tk.Frame):
    def __init__(self, gui):
        tk.Frame.__init__(self, gui.root)
        self.gui = gui
        self.root = gui.root

        self.menu_frame()
        self.bind("<Configure>", self.resize)

    def menu_frame(self) -> None:
        '''
        Initializes menu frame
        '''
        #Sets up the geometry of frame
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

        buttons = [b1, b2, b3, b4]
        self.widgets = [l1, b1, b2, b3, b4]

        l1.grid(row = 0, column = 0, sticky = "NSWE", pady = (0, 80), columnspan = 3)
        #self.grid_rowconfigure(0, weight = 1)
        
        #Packing buttons into grid
        counter = 1
        for i in buttons:
            i.grid(row = counter, column = 1, sticky = "NSWE", pady = 10)

            #self.grid_rowconfigure(counter, weight = 1)
            counter += 1


    def settings_frame(self) -> None:
        '''
        Initializes settings frame
        '''
        self.reset()

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
        f_size = s.ValueSetting("Frame size", "60", self.sett_frame)
        w_size = s.ValueSetting("Window size", "60", self.sett_frame)
        butt = s.OFButton("test", True, self.sett_frame)

        #Packing settings_frame 
        f_size.pack(fill = tk.X, pady = 10)
        w_size.pack(fill = tk.X, pady = 10)
        butt.pack(fill = tk.X, pady = 10)
        

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
            #print(type(i))
            if isinstance(i, (tk.Frame, s.OFButton, s.ValueSetting)): 
                self.frame_resize(i, delta)
            else: 
                i_info = i.cget('font').split(" ")
                if isinstance(i, s.MenuLabel): 
                    new_label = s.resize_info(i_info[0], delta[0])
                else:
                    new_label = s.resize_info(i_info[0], delta[1], True)
                i.configure(font = new_label)
            
            #print("finished that widget")
        #print("finished everything")

    def reset(self) -> None:
        '''
        Cleans up frame
        '''
        self.configure(bg = s.background_theme)
        for widget in self.winfo_children():
            widget.destroy()
        
    def close_win(self):
        self.root.destroy()
