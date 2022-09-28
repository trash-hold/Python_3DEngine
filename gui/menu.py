import tkinter as tk
import gui.styles as s

class Menu(tk.Frame):
    def __init__(self, gui):
        tk.Frame.__init__(self, gui.root)
        self.gui = gui
        self.root = gui.root

        self.x = 0
        self.y = 0

        self.menu_frame()
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        self.x = self.root.winfo_width()
        self.y = self.root.winfo_height()

    def menu_frame(self):
        self.reset()
        tk.Grid.rowconfigure(self, 0, weight = 4, minsize = 40)
        tk.Grid.rowconfigure(self, (1,2,3,4), weight = 1, minsize = 10)
        tk.Grid.columnconfigure(self, 1, weight = 1, minsize = 80)
        tk.Grid.columnconfigure(self, (0, 2), weight = 1, minsize = 50)
                                 
        l1 = s.MenuLabel(self, text = s.menu_banner)

        b1 = s.MenuButton(self, text = "Spin me!", command = self.gui.donut)
        b2 = s.MenuButton(self, text = "Freemode", command = self.freemode_frame)
        b3 = s.MenuButton(self, text = "Settings", command = self.settings_frame)
        b4 = s.MenuButton(self, text = "Exit", command = self.close_win)

        buttons = [b1, b2, b3, b4]
        self.widgets = [l1, b1, b2, b3, b4]

        l1.grid(row = 0, column = 0, sticky = "NSWE", pady = (0, 80), columnspan = 3)
        #self.grid_rowconfigure(0, weight = 1)

        counter = 1
        for i in buttons:
            i.grid(row = counter, column = 1, sticky = "NSWE", pady = 10)

            #self.grid_rowconfigure(counter, weight = 1)
            counter += 1

    def settings_frame(self):
        self.reset()
        self.configure(bg = s.bloody_red)

        

        b1 = s.MenuButton(self, text = "What you looking at?", command = self.menu_frame)
        b1.pack()

    def freemode_frame(self):
        pass

    def reset(self):
        self.configure(bg = "#292929")
        for widget in self.winfo_children():
            widget.destroy()

    def close_win(self):
        self.root.destroy()

        

