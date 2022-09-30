import tkinter as tk
#gotta do sth about those
min_value = 20
max_value = 1000


bloody_red = "#A42929"
light_green = "#27BB73"
jet = "#292929"
jet_black = "#161616"
light_gray = "#4F4F4F"
hacker_green = "#0D8E50"
dark_green = "#066235"

main_theme = hacker_green
background_theme = jet
shadow_main = dark_green
shadow_back = jet_black
highlight_bg = light_green
highlight_fg = light_gray


button_style = ("Terminal", 20)
entry_style = ("Terminal", 20)
label_style = ("Consolas", 7)
setting_label = ("Terminal", 30)

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

class MenuLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self['font'] = label_style
        self['justify'] = tk.LEFT

class SettEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, *args, **kwargs)
        self['bg'] = shadow_main
        self['bd'] = 5
        self['fg'] = background_theme
        self['font'] = entry_style
        self['justify'] = tk.CENTER
        self['relief'] = tk.RIDGE


class ValueSetting(tk.Canvas):
    def __init__(self, label = "Label text", entry = "Entry text", *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.var = tk.StringVar()
        self.default = entry 
        self.var.set(self.default)

        l = MenuLabel(self, text = label)
        l.configure(font = setting_label, bg = bloody_red)
        button_frame = tk.Frame(self)

        self.ent = SettEntry(button_frame, textvariable = self.var)
        vcm = self.register(self.check)
        ivcm = self.register(self.failed_check)
        self.ent.config(validate = "key", validatecommand = (vcm, "%P")) 

        b1 = MenuButton(button_frame, text = "<", command = lambda: self.increment(False))
        b2 = MenuButton(button_frame, text = ">", command = lambda: self.increment())

        widgets = [b1, self.ent, b2]
        for i in widgets:
            i.pack(side = tk.LEFT, padx = (0, 10), fill = tk.Y, pady = 20)

        l.pack(side = tk.LEFT, fill = tk.BOTH, padx = (0, 50))
        button_frame.pack(side = tk.RIGHT)

        """self.grid_columnconfigure(0, weight = 2)
        self.grid_columnconfigure(0, weight = 1)
        l.grid(row = 0, column = 0, sticky = "E")
        button_frame.grid(row = 0, column = 1, sticky = "E", pady = 10)"""

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

    def change_var(self, val):
        self.var.set(val)

    


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