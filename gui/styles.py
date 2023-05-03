import tkinter as tk
#gotta do sth about those
min_value = 20
max_value = 1000

trans = "#B00B15"
bloody_red = "#A42929"
light_green = "#27BB73"
jet = "#292929"
jet_black = "#161616"
light_gray = "#4F4F4F"
gray = "#424242"
hacker_green = "#0D8E50"
dark_green = "#066235"

main_theme = hacker_green
background_theme = jet
shadow_main = dark_green
shadow_back = jet_black
highlight_bg = light_green
highlight_fg = light_gray

display_style = ("DejaVu Sans Mono", 7)
button_style = ("Terminal", 20)
entry_style = ("Terminal", 20)
label_style = ("Consolas", 7)
setting_label = ("Terminal", 20)
big_label = ("Terminal", 40)

labels_height = [button_style, entry_style, setting_label, big_label]
labels_width = [label_style]


class MenuButton(tk.Button):
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

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self['bg'] = highlight_bg
        self['fg'] = highlight_fg
    
    def on_leave(self, event):
        self['bg'] = main_theme
        self['fg'] = background_theme

class DisplayLabel(tk.Label):
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
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['font'] = label_style
        self['justify'] = tk.LEFT

class BigLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['font'] = big_label
        self['justify'] = tk.CENTER

class SettEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, *args, **kwargs)
        self['bg'] = shadow_main
        self['bd'] = 5
        self['fg'] = background_theme
        self['font'] = entry_style
        self['justify'] = tk.CENTER
        self['relief'] = tk.FLAT

class OFButton(tk.Frame):
    def __init__(self, label = "Label", mode = True, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.mode = tk.BooleanVar(value = mode)
        self.img_on = tk.PhotoImage(file = "gui/src/check_on.png")
        self.img_off = tk.PhotoImage(file = "gui/src/check_off.png")
        self.img = None
        
        if mode: self.img = self.img_on
        else: self.img = self.img_off

        self.b = tk.Button(self, image = self.img, command = self.switch, relief = tk.FLAT, activebackground = shadow_main)
        l = tk.Label(self, text = label)

        self.b.pack(side = tk.RIGHT, fill = tk.Y, padx = (0, 40), pady = 10)
        l.pack(side = tk.LEFT, fill = tk.X, padx = (30, 150), pady = 20)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)


    def switch(self):
        if self.mode.get():
            self.b.configure(image = self.img_off)
            self.mode.set(False)
        else:
            self.b.configure(image = self.img_on)
            self.mode.set(True)

    def on_enter(self, event):
        for i in self.winfo_children():
            i.configure(bg = gray)
        self.configure(bg = gray)
    
    def on_leave(self, event):
        for i in self.winfo_children():
            i.configure(bg = background_theme)
        self.configure(bg = background_theme)



class ValueSetting(tk.Frame):
    def __init__(self, label = "Label text", entry = "Entry text", *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.var = tk.StringVar()
        self.default = entry 
        self.var.set(self.default)

        l = tk.Label(self, text = label)
        #l.configure(font = setting_label)
        button_frame = tk.Frame(self)
        self.wid_active = [l, button_frame, self]

        self.ent = SettEntry(button_frame, textvariable = self.var)
        vcm = self.register(self.check)
        ivcm = self.register(self.failed_check)
        self.ent.config(validate = "key", validatecommand = (vcm, "%P")) 

        b1 = MenuButton(button_frame, text = "-", command = lambda: self.increment(False))
        b2 = MenuButton(button_frame, text = "+", command = lambda: self.increment())

        widgets = [b1, self.ent, b2]
        for i in widgets:
            i.pack(side = tk.LEFT, padx = (0, 0), fill = tk.Y, pady = 20)

        button_frame.pack(side = tk.RIGHT, padx = (0, 15))
        l.pack(side = tk.LEFT, fill = tk.BOTH, padx = (30, 150))

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def increment(self, incr = True):
        inc = 10
        var_value = int(self.var.get())
        if incr: self.var.set(var_value + inc if var_value <= max_value - inc else max_value)
        else: self.var.set(var_value - inc if var_value >= min_value + inc else min_value)

    def check(self, input):
        if input.isdigit():
            val = int(input)
            if val <= max_value and val >= min_value and input[0] != "0":
                return True
        return False

    def failed_check(self, input):
        if input.isdigit():
            val = int(input)
            if input[0] == 0: 
                val = int(input.lstrip("0"))

            if val > max_value: val = max_value
            elif val < min_value: val = min_value
        
        else: val = int(self.default)

    def on_enter(self, event):
        for i in self.wid_active:
            i.configure(bg = gray)
    
    def on_leave(self, event):
        for i in self.wid_active:
            i.configure(bg = background_theme)

    
def resize_info(font, win, big_label = False):
    default = 720 if big_label else 1080
    step = 50 if big_label else 200
    #print("New win: " + str(win))
    min_height = 20 if big_label else 7
    #if big_label:
    if default >= win: return (font, min_height)
    else:
        print(min_height + (win - default) // step)
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