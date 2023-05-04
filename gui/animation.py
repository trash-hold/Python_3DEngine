import tkinter as tk
import gui.styles as s

class Animation(tk.Frame):
    def __init__(self, gui):
            tk.Frame.__init__(self, gui.root)
            self.gui = gui
            self.root = gui.root
            self.stop = False

            self.display()
    
    def display(self):
        '''
        Pre-programmed rotation sequence
        '''
        self.reset_frame()
        top_frame = tk.Frame(self)

        #Initial render from engine
        self.gui.ren.render()
        self.counter = 0
        self.stop = False

        #Creating top_frame widgets
        sett = s.BigLabel(top_frame, text = "Animation")
        sett.configure(bg = s.main_theme, fg = s.background_theme, pady = 10)
        exit = s.MenuButton(top_frame, text = "<")
        exit.configure(relief = tk.FLAT, padx = 20, command = self.return_menu)

        #Packing top_frame
        exit.pack(side = tk.LEFT, padx = (0, 10), fill = tk.Y)
        sett.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

        self.object_img = s.DisplayLabel(self, text = "", width = int(self.gui.win.__wsize__[0]*1.5), height =  int(self.gui.win.__wsize__[1]*2))

        #self.start_butt.pack()
        top_frame.pack(side = tk.TOP, fill = tk.X)
        self.object_img.pack(fill = tk.NONE, pady = 20, padx = 30, expand = True)

        self.animation()
        #self.root.mainloop()
    
    """def update_img(self):
        sleep(self.ren.__refresh_rate__)
        self.image = self.ren.__image__
        if self.counter < 360: 
            if self.counter == 0: self.start_var.set("")
            self.start_butt.invoke()
        self.counter = self.counter + 1"""

    def animation(self) -> None:
        ren = self.gui.ren
        cam = self.gui.cam
        if ((self.counter < 360) and (self.stop == False)):
            ren.render()
            self.object_img.config(text = ren.__image__)
            cam.update_cam(self.gui.win.__obj__)
            cam.rotate([0, -180 + self.counter, -180 + self.counter], True)
            self.counter += 1
            self.root.after(25, self.animation)

    def reset_frame(self) -> None:
        self.configure(bg = s.background_theme)
        for widget in self.winfo_children():
            widget.destroy()
    
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
                if isinstance(i, (s.MenuLabel, s.DisplayLabel)): 
                    new_label = s.resize_info(i_info[0], delta[0])
                else:
                    new_label = s.resize_info(i_info[0], delta[1], True)
                i.configure(font = new_label)

    def return_menu(self):
         self.stop = True
         self.gui.change_frame('Menu')