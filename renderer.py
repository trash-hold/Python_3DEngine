import numpy as np

class Renderer:
    def __init__(self, p):
        self.__render__ = p.__obj__
        self.__size__ = p.__wsize__
        self.__map__ = {(x, y): [] for x in range(int(self.__size__[0])) for y in range(int(self.__size__[1]))}

    def mapping(self):
        # # $ & @ %
        if np.shape(self.__render__)[0] == 0:
            return False
        max_z = np.amax(self.__render__, axis = 0)[2]
        buffer_size = max_z // 7 + 1
        sym = {0: "@", 1: "#", 2: "%", 3: "&", 4: "$", 5: "!", 6: "."}

        #creating map
        mapping = self.__map__
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

    def terminal_print(self):
        print(" " + "__" * int(self.__size__[0]))
        for j in range(int(self.__size__[1])):
            x = "|"
            for i in range(int(self.__size__[0])):
                x = x + " " + self.__map__[i, j]
            print(x + "|")
        print(" " + "--" * int(self.__size__[0]))


    def render(self):
        if self.mapping():
            self.terminal_print()