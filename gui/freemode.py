import tkinter as tk
import gui.styles as s
import engine.shapes as sh

class Freemode(tk.Frame):
    def __init__(self, gui):
        tk.Frame.__init__(self, gui.root)
        self.gui = gui
        self.root = gui.root

        self.fc = FrameCreator(self)

        self.current_mode = 'Donut'

        self.main_frame()

    def main_frame(self):
        self.reset()

        #Creating basic layout
        title_banner = tk.Frame(self, bg = 'red')
        left_panel = tk.Frame(self, bg = 'orange')
        display = tk.Frame(self, bg = 'blue')

        tk.Grid.rowconfigure(self, 0, weight = 0, minsize = 20)
        tk.Grid.rowconfigure(self, 1, weight = 4, minsize = 40)
        tk.Grid.columnconfigure(self, 0, weight = 2, minsize = 200)
        tk.Grid.columnconfigure(self, 1, weight = 6, minsize = 80)

        title_banner.grid(row = 0, column = 0, columnspan = 2, sticky = "NWE")
        left_panel.grid(row = 1, column = 0, sticky = 'NSWE')
        display.grid(row = 1, column = 1, sticky = 'NSWE')

        #Creating title_banner widgets
        self.fc.title_banner_create(title_banner)
        #Creating left_panel
        self.fc.left_panel_create(left_panel)
        #Creating display
        self.fc.display_create(display)
        self.change_mode(self.current_mode)

    def change_mode(self, mode_name):
        self.current_mode = mode_name
        self.fc.sliders_menu(mode_name)
        """self.fc.render_img.config(text = mode_name)
        #THIS FUCKING WORKS !!!!!!!!!!!!!!
        for widget in self.fc.settings_frame.winfo_children():
            widget.destroy()

        b1 = s.MenuButton(self.fc.settings_frame, text = mode_name)
        b1.pack(side = tk.TOP, expand = True, fill = tk.X)"""

    def reset(self, frame = None) -> None:
        '''
        Cleans up frame
        '''
        if frame is None: frame = self

        frame.configure(bg = s.background_theme)
        for widget in frame.winfo_children():
            widget.destroy()


class FrameCreator():
    def __init__(self, parent):
        self.parent = parent
        self.gui = parent.gui

        self.render_img = None
        self.settings_frame = None

    def title_banner_create(self, title_banner: tk.Frame) -> None:
        #Creating widgets
        sett = s.BigLabel(title_banner, text = "Settings")
        sett.configure(bg = s.main_theme, fg = s.background_theme, pady = 10)
        exit = s.MenuButton(title_banner, text = "<")
        exit.configure(relief = tk.FLAT, padx = 20, command=lambda: self.gui.change_frame('Menu'))

        next = s.MenuButton(title_banner, text = ">")
        next.configure(relief = tk.FLAT, padx = 20, command = print('implement me!'))

        #Packing title_banner
        exit.pack(side = tk.LEFT, padx = (0, 10), fill = tk.Y)
        next.pack(side = tk.RIGHT, padx = (10, 0), fill = tk.Y)
        sett.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
    
    def left_panel_create(self, left_panel: tk.Frame)-> None:
        #Creating smaller container for buttons
        button_container = tk.Frame(left_panel, bg = 'green', pady = 40, padx = 20)
        
        #Creating grid
        tk.Grid.rowconfigure(button_container, (0, 1, 2, 3), weight = 1, minsize = 40)
        tk.Grid.columnconfigure(button_container, 0, weight = 2, minsize = 80)
        
        #Creating widgets
        donut_butt = s.MenuButton(button_container, text = 'Donut', command = lambda: self.parent.change_mode('Donut'))
        sphere_butt = s.MenuButton(button_container, text = 'Sphere', command = lambda: self.parent.change_mode('Sphere'))
        cube_butt = s.MenuButton(button_container, text = 'Cube', command = lambda: self.parent.change_mode('Cube'))
        circle_butt = s.MenuButton(button_container, text = 'Circle', command = lambda: self.parent.change_mode('Circle'))

        #Packing buttons
        buttons = [donut_butt, sphere_butt, cube_butt, circle_butt]
        for i in range(0, len(buttons)):
            buttons[i].grid(row = i, column = 0, sticky = "nesw", pady = [0, 20])

        #Packing container
        button_container.pack(fill = tk.BOTH, expand = True)

    def display_create(self, display: tk.Frame) -> None:
        display_container = tk.Frame(display, bg = 'orange', padx = 20, pady = 30)
        tk.Grid.rowconfigure(display_container, 0, weight = 1, minsize = 20)
        tk.Grid.rowconfigure(display_container, 1, weight = 0, minsize = 40)
        tk.Grid.columnconfigure(display_container, 0, weight = 1, minsize = 80)
        tk.Grid.columnconfigure(display_container, 1, weight = 0, minsize = 80)

        self.render_img = s.DisplayLabel(display_container, text = 'Render')
        done_butt = s.MenuButton(display_container, text = 'Done', command=lambda: self.parent.gui.change_frame('Animation'))

        self.settings_frame = tk.Frame(display_container, bg = 'red', padx = 10, pady = 20)

        self.render_img.grid(row = 0, column = 0, sticky = 'NSEW')
        self.settings_frame.grid(row = 0, column = 1, sticky = 'NSEW')
        done_butt.grid(row = 1, column = 1, sticky = 'NSE', pady = [30, 0])

        display_container.pack(fill = tk.BOTH, expand = True)

    def sliders_menu(self, mode: str):
        #Clearing the frame
        for widget in self.settings_frame.winfo_children():
                widget.destroy()
        
        values = {}
        obj_value = None
        
        if mode == 'Donut': 
            label1 = 'Radius R'
            min_max1 = [10, 400]
            default_val1 = 250

            label2 = 'Radius r'
            min_max2 = [0, 200]
            default_val2 = 80
            obj_value = [default_val1, default_val2]

            slider_R = s.SettingsSlider(master = self.settings_frame, label = label1, values = min_max1)
            slider_R.set_value(default_val1)

            slider_r = s.SettingsSlider(master = self.settings_frame, label = label2, values = min_max2)
            slider_r.set_value(default_val2)

            slider_R.pack(side = tk.TOP, fill = tk.X, anchor = tk.N, pady = 20)
            slider_r.pack(side = tk.TOP, fill = tk.X, anchor = tk.N, pady = 20)

        elif mode in ('Cube', 'Sphere', 'Circle'):
            label = ''
            min_max = None
            default_val = None
            match mode:
                case 'Cube':
                    label = 'Length A'
                    min_max = [10, 300]
                    default_val = 100
                    obj_value = [default_val]
                case 'Sphere':
                    label = 'Radius R'
                    min_max = [10, 100]
                    default_val = 50
                    obj_value = [default_val]
                case 'Circle':
                    label = 'Radius R'
                    min_max = [10, 400]
                    default_val = 200
                    obj_value = [default_val]

            slider = s.SettingsSlider(master = self.settings_frame, label = label, values = min_max)
            slider.set_value(default_val)

            slider.pack(side = tk.TOP, fill = tk.X, anchor = tk.N, pady = 20)

        else: raise NotImplementedError('GUIerr: Trying to invoke wrong settings_frame mode')

        save_button = s.MenuButton(self.settings_frame, text = 'Save')
        save_button.pack(fill = tk.X, side = tk.BOTTOM, anchor = tk.S, pady = [0, 10], padx = 20)

        self.update_render(mode, obj_value)

    
    def update_render(self, mode: str, value: list()):
        shape = None
        match mode:
            case 'Donut':
                shape = sh.Donut(value)
                shape.rotate([0, 45, 45])
            case 'Cube':
                shape = sh.Cube(value)
                shape.rotate([0, 45, 45])   
            case 'Sphere':
                shape = sh.Sphere(value)
            case 'Circle':
                shape = sh.Circle(value)
                shape.rotate([0, 45, 45])

        self.gui.cam.update_obj(shape.__obj__)
        self.gui.win.update_obj(shape.__obj__)
        self.gui.ren.render()
        self.render_img.config(text = self.gui.ren.__image__)
