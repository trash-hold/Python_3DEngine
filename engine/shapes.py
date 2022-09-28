from lib.math_lib import *

class Shape:
    def __init__(self, dim, origin):
        self.__obj__ = None
        self.__origin__ = origin
        self.__dim__ = dim

        self.draw()
    
    def draw(self):
        pass

    def show(self):
        print(self.__obj__)

    def rotate(self, rot, new_origin = False):
        #rot    - list/vector containing three angles (in degrees) descibing rotation (OX, OY, OZ)
        if new_origin is not False: new_origin = np.array([0, 0, 0])
        else: new_origin = self.__origin__

        rot[0] = m.radians(rot[0])
        rot[1] = m.radians(rot[1])
        rot[2] = m.radians(rot[2])

        rot_phi = np.array([[m.cos(rot[0]), m.sin(rot[0]), 0],
                        [-m.sin(rot[0]), m.cos(rot[0]), 0],
                        [0, 0, 1]])

        rot_theta = np.array([[m.cos(rot[1]), 0 , -m.sin(rot[1])],
                        [0, 1, 0],
                        [m.sin(rot[1]), 0, m.cos(rot[1])]])
    
        rot_psi = np.array([[1, 0, 0],
                        [0, m.cos(rot[2]), m.sin(rot[2])],
                        [0, -m.sin(rot[2]), m.cos(rot[2])]])
    
        rot_mat = np.dot(rot_phi, np.dot(rot_theta, rot_psi))
        if False: print(rot_mat)

        self.__obj__ = np.dot((self.__obj__- self.__origin__ + new_origin), rot_mat) - new_origin + self.__origin__

    def move(self, vec):
        self.__obj__ = self.__obj__ + vec


class Circle(Shape):
    def __init__(self, dim, origin = np.array([0, 0, 0])):
        super().__init__(dim, origin)
    
    def draw(self):
        if len(self.__dim__) != 1: raise ValueError("ErrV5: Not enough data to draw figure")
        if self.__origin__.shape[0] != 3: raise ValueError("ErrV6: Invalid origin coordinates") 

        obj = None
        dim = self.__dim__
        for x in range(-dim[0], dim[0]):
            if obj is None:
                obj = np.array([[x, m.sqrt(dim[0]*dim[0] - x*x), 0], [-x, m.sqrt(dim[0]*dim[0] - x*x), 0]])
            else:
                new_obj = np.array([[x, m.sqrt(dim[0]*dim[0] - x*x), 0], [x, -m.sqrt(dim[0]*dim[0] - x*x), 0]])
                obj = np.vstack([obj, new_obj])

        #Function draws around (0, 0, 0) point and then moves figure to the right origin point 
        self.__obj__ = obj + self.__origin__

class Donut(Shape):
    def __init__(self, dim, origin = np.array([0, 0, 0])):
        super().__init__(dim, origin)
    
    def draw(self):
        #first dim is bigger radius R, second is small r
        if len(self.__dim__) != 2: raise ValueError("ErrV5: Not enough data to draw figure")
        if self.__origin__.shape[0] != 3: raise ValueError("ErrV6: Invalid origin coordinates") 

        obj = None
        dim = self.__dim__

        for alpha in range(0, 360, 2):
            alpha = m.radians(alpha)
            const = dim[0] + dim[1] * m.cos(alpha)
            const2 = dim[1] * m.sin(alpha)

            for beta in range(0, 360, 2):
                beta = m.radians(beta)
                vec = np.array([const * m.cos(beta), const * m.sin(beta), const2])

                if obj is None:
                    obj = vec 
                else: 
                    obj = np.vstack([obj, vec])
        
        self.__obj__ = obj + self.__origin__

        