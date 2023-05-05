import tkinter as tk
from PIL import Image, ImageTk

'''
Styles holds information about appearance of widgets (colour hexes etc) and keep custom widgets that inherit from tkinter
'''

#Constants
min_value = 20
max_value = 1000
#####################################################



#Colours' hexes
trans = "#B00B15"
bloody_red = "#A42929"
light_green = "#27BB73"
jet = "#292929"
jet_black = "#161616"
light_gray = "#4F4F4F"
gray = "#424242"
hacker_green = "#0D8E50"
dark_green = "#066235"
#####################################################



#Themes
main_theme = hacker_green
background_theme = jet
shadow_main = dark_green
shadow_back = jet_black
highlight_bg = light_green
highlight_fg = light_gray
#####################################################



#Fonts
display_style = ("DejaVu Sans Mono", 7)
button_style = ("Terminal", 20)
entry_style = ("Terminal", 20)
label_style = ("Consolas", 7)
setting_label = ("Terminal", 20)
big_label = ("Terminal", 40)
header = ("Terminal", 24)
#####################################################



#Buttons
class MenuButton(tk.Button):
    '''
    Button used throughout the code, mainly in main menu frame
    '''
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self['bg'] = main_theme
        self['fg'] = background_theme
        self['pady'] = 10
        self['padx'] = 10
        self['font'] = button_style
        self['relief'] = tk.RIDGE
        self['activebackground'] = shadow_main
        self['activeforeground'] = shadow_back

        #Binds for changing button colour while in focus
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self['bg'] = highlight_bg
        self['fg'] = highlight_fg
    
    def on_leave(self, event):
        self['bg'] = main_theme
        self['fg'] = background_theme




class OFButton(tk.Frame):
    '''
    On/Off button with label
    '''
    def __init__(self, label = "Label", mode = True, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        #Setting up button variables
        self.mode = tk.BooleanVar(value = mode)
        
        #Loading images
        open_imgOn = Image.open('gui/src/check_on.png')
        open_imgOff = Image.open('gui/src/check_off.png')

        width = 40
        height = 40
        open_imgOn = open_imgOn.resize((width, height), Image.ANTIALIAS)
        open_imgOff = open_imgOff.resize((width, height), Image.ANTIALIAS)

        self.img_on = ImageTk.PhotoImage(open_imgOn)
        self.img_off = ImageTk.PhotoImage(open_imgOff)
        self.img = None
        
        if mode: self.img = self.img_on
        else: self.img = self.img_off

        #Creating widgets
        self.b = tk.Button(self, image = self.img, command = self.switch, relief = tk.FLAT, activebackground = shadow_main)
        label = tk.Label(self, text = label, font = setting_label)

        #Packing widgets
        self.b.pack(side = tk.RIGHT, padx = (0, 40), pady = 10)
        label.pack(side = tk.LEFT, fill = tk.X, padx = (30, 150), pady = 20)

        #Highlighting while in focus
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def get_value(self) -> bool:
        '''
        Returns the state of the button
        '''
        return self.mode.get()
    

    def switch(self) -> None:
        '''
        Changes (bool) value and image of button
        '''
        if self.mode.get():
            self.b.configure(image = self.img_off)
            self.mode.set(False)
        else:
            self.b.configure(image = self.img_on)
            self.mode.set(True)

    def on_enter(self, event) -> None:
        for i in self.winfo_children():
            i.configure(bg = gray)
        self.configure(bg = gray)
    
    def on_leave(self, event) -> None:
        for i in self.winfo_children():
            i.configure(bg = background_theme)
        self.configure(bg = background_theme)


############################################################################################



#Labels
class DisplayLabel(tk.Label):
    '''
    Used to display rendered image
    '''
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['bg'] = shadow_back
        self['fg'] = highlight_bg
        self['font'] = display_style
        self['justify'] = tk.CENTER
        self['relief'] = tk.RIDGE
        self['padx'] = 180
        self['pady'] = 10



class MenuLabel(tk.Label):
    '''
    Used to display title in main_menu
    '''
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['font'] = label_style
        self['justify'] = tk.LEFT



class BigLabel(tk.Label):
    '''
    Used to display headers
    '''
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['font'] = big_label
        self['justify'] = tk.CENTER


############################################################################################



#Other widgets
class SettEntry(tk.Entry):
    '''
    Entry widget used in settings frame
    '''
    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, *args, **kwargs)
        self['bg'] = shadow_main
        self['bd'] = 5
        self['fg'] = background_theme
        self['font'] = entry_style
        self['justify'] = tk.CENTER
        self['relief'] = tk.FLAT



class Slider(tk.Scale):
    '''
    Slider used in freemode frame's control panel
    '''
    def __init__(self, *args, **kwargs):
        tk.Scale.__init__(self, *args, **kwargs)
        self['bg'] = gray
        self['fg'] = main_theme
        self['troughcolor'] = main_theme
        self['font'] = button_style
        self['showvalue'] = 1
        self['orient'] = tk.HORIZONTAL
        self['relief'] = tk.FLAT
        self['highlightthickness'] = 0

############################################################################################




#Frames
class ValueSetting(tk.Frame):
    '''
    Setting frame that consists of label, increment and decrement buttons, entry
    '''
    def __init__(self, master, label, entry, _min = min_value, _max = max_value, *args, **kwargs):
        tk.Frame.__init__(self, master = master, *args, **kwargs)
        self.min = _min
        self.max = _max
        
        #Setting up entry
        self.var = tk.StringVar()
        self.default = entry 
        self.var.set(self.default)

        #Creating label
        l = tk.Label(self, text = label, font = setting_label)

        #Creating buttons
        button_frame = tk.Frame(self)
        b1 = MenuButton(button_frame, text = "-", command = lambda: self.increment(False))
        b2 = MenuButton(button_frame, text = "+", command = lambda: self.increment())

        #Helper list
        self.wid_active = [l, button_frame, self]

        #Creating entry
        self.ent = SettEntry(button_frame, textvariable = self.var)
        vcm = self.register(self.check)
        ivcm = self.register(self.failed_check)
        self.ent.config(validate = "key", validatecommand = (vcm, "%P")) 

        #Packing widgets
        widgets = [b1, self.ent, b2]
        for i in widgets:
            i.pack(side = tk.LEFT, padx = (0, 0), fill = tk.Y, pady = 20)

        #Packing frames
        button_frame.pack(side = tk.RIGHT, padx = (0, 15))
        l.pack(side = tk.LEFT, fill = tk.BOTH, padx = (30, 150))

        #Highlighting frame while in focus 
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)


    def get_value(self) -> int:
        '''
        Returns the value of the entry
        '''
        if self.check(self.ent.get()):
            return int(self.var.get())
        

    def increment(self, incr: bool = True) -> None:
        '''
        Changes value of entry
        '''
        inc = 10
        var_value = int(self.var.get())
        if incr: 
            self.var.set(var_value + inc if var_value <= self.max - inc else self.max)
        else: 
            self.var.set(var_value - inc if var_value >= self.min + inc else self.min)

    def check(self, input) -> bool:
        '''
        Validates user input
        '''
        if input.isdigit():
            val = int(input)
            if val <= self.max and val >= self.min and input[0] != "0":
                return True
        return False

    def failed_check(self, input) -> None:
        '''
        Handles failed check
        '''
        if input.isdigit():
            val = int(input)
            if input[0] == 0: 
                val = int(input.lstrip("0"))

            if val > self.max: val = self.max
            elif val < self.min: val = self.min
        
        else: val = int(self.default)

    def on_enter(self, event):
        for i in self.wid_active:
            i.configure(bg = gray)
    
    def on_leave(self, event):
        for i in self.wid_active:
            i.configure(bg = background_theme)




class SettingsSlider(tk.Frame):
    '''
    Setting slider, consists of label and slider
    '''
    def __init__(self, master, label, values, *args, **kwargs):
        tk.Frame.__init__(self, master = master, *args, **kwargs)
        self.config(bg = gray, relief = tk.FLAT)

        #Creating widgets
        self.slider = Slider(self, from_ = values[0], to = values[1])
        lab = tk.Label(self, text = label, justify= tk.LEFT, font = setting_label, bg = gray )

        #Packing widgets
        self.slider.pack(side = tk.RIGHT, fill = tk.Y, padx = (0, 20), anchor = tk.SW, expand = True)
        lab.pack(side = tk.LEFT, padx = (20, 40), anchor = tk.SE, fill = tk.X)

    def get_value(self) -> int:
        '''
        Returns the value of slider
        '''
        return int(self.slider.get())
    
    def set_value(self, value: int):
        '''
        Sets slider to given value
        '''
        self.slider.set(value = value)
    
############################################################################################




#Helper functions
def resize_info(font, win, big_label = False) -> tuple:
    '''
    Return appropriate tuple (font, font_size) for given window size 
    '''
    default = 720 if big_label else 1080
    step = 50 if big_label else 200
    min_height = 20 if big_label else 7
    if default >= win: return (font, min_height)
    else:
        return (font, min_height + (win - default) // step)

menu_banner = """                                                                                                                                                                             
                 8 888888888o.   8 8888888888            .8.          8 8888                 8 8888888888   b.             8     ,o888888o.     8 8888  8 8888 b.             8 8 88888888888888   
                8 8888    `88.  8 8888                 .888.         8 8888                 8 8888         888o.          8    8888     `88.   8 8888  8 8888 888o.          8 8 8888         
               8 8888     `88  8 8888                :88888.        8 8888                 8 8888         Y88888o.       8 ,8 8888       `8.  8 8888  8 8888 Y88888o.       8 8 8888         
              8 8888     ,88  8 8888               . `88888.       8 8888                 8 8888         .`Y888888o.    8 88 8888            8 8888  8 8888 .`Y888888o.    8 8 8888         
             8 8888.   ,88'  8 888888888888      .8. `88888.      8 8888                 8 888888888888 8o. `Y888888o. 8 88 8888            8 8888  8 8888 8o. `Y888888o. 8 8 888888888888 
            8 888888888P'   8 8888             .8`8. `88888.     8 8888                 8 8888         8`Y8o. `Y88888o8 88 8888            8 8888  8 8888 8`Y8o. `Y88888o8 8 8888         
           8 8888`8b       8 8888            .8' `8. `88888.    8 8888                 8 8888         8   `Y8o. `Y8888 88 8888   8888888  8 8888  8 8888 8   `Y8o. `Y8888 8 8888         
          8 8888 `8b.     8 8888           .8'   `8. `88888.   8 8888                 8 8888         8      `Y8o. `Y8 `8 8888       .8'  8 8888  8 8888 8      `Y8o. `Y8 8 8888         
         8 8888   `8b.   8 8888          .888888888. `88888.  8 8888                 8 8888         8         `Y8o.`    8888     ,88'   8 8888  8 8888 8         `Y8o.` 8 8888         
        8 8888     `88. 8 888888888888 .8'       `8. `88888. 8 888888888888         8 888888888888 8            `Yo     `8888888P'     8 8888  8 8888 8            `Yo 8 888888888888
"""