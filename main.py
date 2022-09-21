from logging import raiseExceptions
import numpy as np
import math as m
from shapes import Circle

__frame_size__ = 100 
class Window:
    def __init__(self, w_sizeX = 60, w_sizeY = 60, win_rules = ["center", "adjust"], shapes = None, obj = None, init = False):
        """
        w_size - width and height of render in terminal; int > 1
        obj - matrix of points' coordinates (x,y,z) in a form of matrix size (N, 3) 
        win_rules - set of rules which define how camera is gonna work; must be dictionary keys
        """
        #Private variables
        self.__wsize__ = None
        self.__shapes__ = None
        self.__obj__ = None 
        self.__rules__ = {"center": False, "adjust": False, "z_red": False}        

        if (init == False):
            #Intialising window size vector 
            if isinstance(w_sizeX, int) and isinstance(w_sizeY, int):
                if w_sizeX > 1 and w_sizeY > 1: self.__wsize__ = np.array([w_sizeX, w_sizeY, 1]).T
                else: raise ValueError("ErrV2: Window size can't be smaller than 1px")
            else:
                    #raise ValueError("ErrV1: Window sizes must be integers")
                    print("Problem with remaking it into vector after inheriting from child")

            #SHAPES IN PROGRESS

            #Initialising object matrix
            if obj is not None:
                if isinstance(obj, np.ndarray): 
                    if np.shape(obj)[0] == 3: self.__object__ = obj
                    else: raise ValueError("ErrV4: Input matrix has wrong data format")
                else: raise ValueError("ErrV3: Input object isn't in matrix form")

            #Initialising rule set
            if isinstance(win_rules, str): win_rules = [win_rules]
            elif win_rules is None: win_rules = []
            for i in win_rules:
                if i in self.__rules__.keys(): self.__rules__[i] = True
                else: raise ValueError("ErrV4: Non existing key word for window")
        else:
            self.__wsize__ = np.array([w_sizeX, w_sizeY, 1])
            self.__shapes__ = shapes
            self.__obj__ = obj 
            self.__rules__ = win_rules 
        
        #Public variables
        self.camera = None
        self.renderer = None
    
    def update_obj(self, obj):
        self.__obj__ = obj

    def get_obj(self):
        return self.__obj__

    def get_wsize(self):
        return self.__wsize__