from lib.math_lib import np

from os import name, system
from time import sleep


class Renderer:
    def __init__(self, p):
        self.__camera__ = p
        self.__render__ = p.__obj__
        self.__size__ = p.__wsize__
        self.__map__ = None
        self.__refresh_rate__ = 0.1

        self.__image__ = None

    
    def render(self):
        self.__camera__.rasterization()
        self.__render__ = self.__camera__.__obj__
        if self.mapping():
            self.tk_print()

    def mapping(self):
        # # $ & @ %
        if np.shape(self.__render__)[0] == 0:
            return False
        max_z = np.amax(self.__render__, axis = 0)[2]
        buffer_size = max_z // 7 + 1
        sym = {0: "@", 1: "%", 2: "0", 3: "1", 4: "=", 5: ",", 6: "."}

        #creating map
        mapping = {(x, y): [] for x in range(int(self.__size__[0])) for y in range(int(self.__size__[1]))}
        for i in self.__render__:
            mapping[(i[0], i[1])].append(i[2])
        
        #rewritting map into symbols
        for i in mapping:
            if mapping[i] == []:
                mapping[i] = " "
            else:
                z = mapping[i]
                mapping[i] = sym[sorted(z)[0]//buffer_size]

        self.__map__ = mapping
        return True

    def tk_print(self):
        render = ""
        for j in range(int(self.__size__[1])):
            x = "|"
            for i in range(int(self.__size__[0])):
                x = x + " " + self.__map__[i, j]
            render = render + x + "|" + "\n"
        #render = render + " " + "--" * int(self.__size__[0])

        self.__image__ = render


    def animate(self):
        cam = self.__camera__
        for i in range(-180, 180, 2):
            self.render()
            #sleep(self.__refresh_rate__)
            #self.clear()
            cam.cam_reset()
            cam.rotate([0, i, i], True)


    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')