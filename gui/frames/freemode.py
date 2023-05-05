from lib.tkinter_lib import *
import engine.shapes as sh

class Freemode(tk.Frame):
    '''
    Frame that:
        - displays rendered preview 
        - lets user edit and pick rendered objects
        - communicates with main menu and animation frames
    Consists of 3 main frames: title_banner (top widget), left_panel (buttons with object options), display (rendered preview + obj customization)
    '''
    def __init__(self, gui):
        tk.Frame.__init__(self, gui.root)
        self.gui = gui
        self.root = gui.root

        self.fc = FrameCreator(self)
        self.current_mode = 'Donut'

        self.main_frame()

    def main_frame(self) -> None:
        self.reset()

        #Creating the main frames
        title_banner = tk.Frame(self, bg = s.dark_green)
        left_panel = tk.Frame(self)
        display = tk.Frame(self)

        #Configuring the geometry
        tk.Grid.rowconfigure(self, 0, weight = 0, minsize = 20)
        tk.Grid.rowconfigure(self, 1, weight = 4, minsize = 40)
        tk.Grid.columnconfigure(self, 0, weight = 2, minsize = 200)
        tk.Grid.columnconfigure(self, 1, weight = 6, minsize = 80)

        #Packing frames
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

    def change_mode(self, mode_name) -> None:
        '''
        Refreshes display's control panel
        '''
        self.current_mode = mode_name
        self.fc.sliders_menu(mode_name)

    def reset(self, frame = None) -> None:
        '''
        Cleans up frame
        '''
        if frame is None: frame = self

        frame.configure(bg = s.background_theme)
        for widget in frame.winfo_children():
            widget.destroy()

###########################################################################################




class FrameCreator():
    '''
    Helper class that cooperates with freemode:
        - creates frames
        - handles actions of widgets
    '''
    def __init__(self, parent):
        self.parent = parent
        self.gui = parent.gui

        #For easier accesss to edited widgets
        self.render_img = None
        self.settings_frame = None

        #IntVars that sit in sliders
        self.val1 = tk.IntVar()
        self.val2 = tk.IntVar()



    def title_banner_create(self, title_banner: tk.Frame) -> None:
        '''
        Creates the title_banner
        '''
        #Creating widgets
        sett = s.BigLabel(title_banner, text = "Freemode")
        exit = s.MenuButton(title_banner, text = "<")
        next = s.MenuButton(title_banner, text = ">")

        #Configuring widgets
        sett.configure(bg = s.main_theme, fg = s.background_theme, pady = 10)
        exit.configure(relief = tk.FLAT, padx = 20, command=lambda: self.gui.change_frame('Menu'))
        next.configure(relief = tk.FLAT, padx = 20, command=lambda: self.gui.change_frame('Animation'))

        #Packing title_banner
        exit.pack(side = tk.LEFT, padx = (0, 10), fill = tk.Y)
        next.pack(side = tk.RIGHT, padx = (10, 0), fill = tk.Y)
        sett.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
    



    def left_panel_create(self, left_panel: tk.Frame)-> None:
        '''
        Creates the left panel frame
        '''
        #Creating smaller container for buttons
        button_container = tk.Frame(left_panel, bg = s.dark_green, pady = 40, padx = 20)
        
        #Creating grid
        tk.Grid.rowconfigure(button_container, (0, 1, 2, 3), weight = 0, minsize = 40, pad = 40)
        tk.Grid.columnconfigure(button_container, 0, weight = 1, minsize = 10)
        
        #Creating widgets
        donut_butt = s.MenuButton(button_container, text = 'Donut', command = lambda: self.parent.change_mode('Donut'))
        sphere_butt = s.MenuButton(button_container, text = 'Cut Sphere', command = lambda: self.parent.change_mode('Sphere'))
        cube_butt = s.MenuButton(button_container, text = 'Cube', command = lambda: self.parent.change_mode('Cube'))
        circle_butt = s.MenuButton(button_container, text = 'Circle', command = lambda: self.parent.change_mode('Circle'))

        #Packing buttons
        buttons = [donut_butt, sphere_butt, cube_butt, circle_butt]
        for i in range(0, len(buttons)):
            buttons[i].grid(row = i, column = 0, sticky = "new")

        #Packing container
        button_container.pack(fill = tk.BOTH, expand = True)




    def display_create(self, display: tk.Frame) -> None:
        '''
        Creates the display frame
        '''
        #Main frame
        display_container = tk.Frame(display, padx = 40, pady = 40)

        #Creating basic geometry
        tk.Grid.rowconfigure(display_container, 0, weight = 1, minsize = 20)
        tk.Grid.rowconfigure(display_container, 1, weight = 0, minsize = 40)
        tk.Grid.columnconfigure(display_container, 0, weight = 1, minsize = 80, pad = 10)
        tk.Grid.columnconfigure(display_container, 1, weight = 0, minsize = 80, pad = 10)

        #Creating widgets
        self.render_img = s.DisplayLabel(display_container, text = 'Render')
        done_butt = s.MenuButton(display_container, text = 'Spin me!')
        self.settings_frame = tk.Frame(display_container)

        #Configuring widgets
        self.render_img.config(padx = 20)
        done_butt.config(command=lambda: self.parent.gui.change_frame('Animation'))
        self.settings_frame.config(bg = s.gray, padx = 20, pady = 20, bd = 2, relief = tk.RIDGE)

        #Packing widgets
        self.render_img.grid(row = 0, column = 0, sticky = 'NSEW')
        self.settings_frame.grid(row = 0, column = 1, sticky = 'NSEW')
        done_butt.grid(row = 1, column = 1, sticky = 'NSE', pady = [30, 0])

        #Packing the frame
        display_container.pack(fill = tk.BOTH, expand = True)

    
    
    def sliders_menu(self, mode: str):
        '''
        Creates the control panel of display
        '''
        #Clearing the frame
        for widget in self.settings_frame.winfo_children():
                widget.destroy()
        
        values = {}
        obj_value = None
        
        #Adding top label
        title_label = s.BigLabel(self.settings_frame, text = 'Shape parameters', anchor = tk.N)
        title_label.config(font = s.header, bg = s.gray)
        title_label.pack(fill = tk.Y, side = tk.TOP)

        #For scalability
        if mode == 'Donut': 
            #Additional variables for clearer code
            label1 = 'Radius R'
            min_max1 = [10, 400]
            default_val1 = 250

            label2 = 'Radius r'
            min_max2 = [0, 200]
            default_val2 = 80
            obj_value = [default_val1, default_val2]

            #Setting sliders to default to avoid init glitches
            self.val1.set(default_val1)
            self.val2.set(default_val2)

            #Creating sliders
            slider_R = s.SettingsSlider(master = self.settings_frame, label = label1, values = min_max1)
            slider_R.set_value(default_val1)

            slider_r = s.SettingsSlider(master = self.settings_frame, label = label2, values = min_max2)
            slider_r.set_value(default_val2)

            #Configuring sliders
            slider_R.slider.config(variable = self.val1, command = lambda value: self.update_render(mode, [int(value), self.val2.get()]))
            slider_r.slider.config(variable = self.val2, command = lambda value: self.update_render(mode, [self.val1.get(), int(value)]))

            #Packing sliders
            slider_R.pack(side = tk.TOP, fill = tk.X, anchor = tk.N, pady = 20)
            slider_r.pack(side = tk.TOP, fill = tk.X, anchor = tk.N, pady = 20)

        elif mode in ('Cube', 'Sphere', 'Circle'):
            #For better scalability
            label = ''
            min_max = None
            default_val = None
            match mode:
                case 'Cube':
                    label = 'Length A'
                    min_max = [10, 110]
                    default_val = 50
                    obj_value = [default_val]
                case 'Sphere':
                    label = 'Radius R'
                    min_max = [10, 200]
                    default_val = 50
                    obj_value = [default_val]
                case 'Circle':
                    label = 'Radius R'
                    min_max = [10, 600]
                    default_val = 300
                    obj_value = [default_val]

            #Creating slider
            slider = s.SettingsSlider(master = self.settings_frame, label = label, values = min_max)
            slider.slider.config(variable = self.val1, command = lambda value: self.update_render(mode, [int(value)]))
            slider.set_value(default_val)

            #Packing slider
            slider.pack(side = tk.TOP, fill = tk.X, anchor = tk.N, pady = 20)

        else: raise NotImplementedError('GUIerr: Trying to invoke wrong settings_frame mode')

        #Creating and packing save button
        save_button = s.MenuButton(self.settings_frame, text = 'Save', command = lambda: self.update_values(mode = mode))
        save_button.pack(fill = tk.X, side = tk.BOTTOM, anchor = tk.S, pady = [0, 10], padx = 20)

        #Refreshing preview
        self.update_render(mode, obj_value)



    def update_values(self, mode: str, *args, **kwargs) -> None:
        '''
        Saves current setting and refreshes preview
        '''
        if mode == 'Donut':
            val = [self.val1.get(), self.val2.get()]
        else:
            val = [self.val1.get()]

        self.update_render(mode, val)
            

    def update_render(self, mode: str, value: list()) -> None:
        '''
        Creates obj and renders it into preview
        '''
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
                shape.rotate([0, 45, 45])
            case 'Circle':
                shape = sh.Circle(value)
                shape.rotate([0, 45, 45])

        #Updating engine
        self.gui.cam.update_obj(shape.__obj__)
        self.gui.win.update_obj(shape.__obj__)

        #Rendering
        self.gui.ren.render()
        self.render_img.config(text = self.gui.ren.__image__)
