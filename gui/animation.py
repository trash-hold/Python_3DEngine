import tkinter as tk
import gui.styles as s

class Animation(tk.Frame):
    def __init__(self, gui):
            tk.Frame.__init__(self, gui.root)
            self.gui = gui
            self.root = gui.root

            self.display()

    def display(self):
        '''
        Pre-programmed rotation sequence
        '''
        self.reset_frame()
        top_frame = tk.Frame(self.root)

        #Initial render from engine
        self.gui.ren.render()
        self.counter = 0

        #Creating top_frame widgets
        sett = s.BigLabel(top_frame, text = "Animation")
        sett.configure(bg = s.main_theme, fg = s.background_theme, pady = 10)
        exit = s.MenuButton(top_frame, text = "<")
        exit.configure(relief = tk.FLAT, padx = 20, command = self.gui.return_menu)

        #Packing top_frame
        exit.pack(side = tk.LEFT, padx = (0, 10), fill = tk.Y)
        sett.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

        self.object_img = s.DisplayLabel(self.root, text = "", width = int(self.gui.win.__wsize__[0]*1.5), height =  int(self.gui.win.__wsize__[1]*2))

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

    def animation(self):
        ren = self.gui.ren
        cam = self.gui.cam
        if self.counter < 360:
            ren.render()
            self.object_img.config(text = ren.__image__)
            cam.cam_reset()
            cam.rotate([0, -180 + self.counter, -180 + self.counter], True)
            self.counter += 1
            self.root.after(25, self.animation)

    def reset_frame(self):
        self.configure(bg = s.background_theme)
        for widget in self.winfo_children():
            widget.destroy()