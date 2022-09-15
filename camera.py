from shapes import Shape
from main import Window
import numpy as np

__frame_size__ = 100


class Camera(Window, Shape):
    def __init__(self, p):
        super().__init__(p.__wsize__[0], p.__wsize__[1], p.__rules__, p.__shapes__, p.__obj__, True)
    
    def cs_transform(self, trans_mat):
        """
        transformation from global cs to camera cs
        points      - matrix containing all objects mesh points
        trans_mat   - matrix consisting of two vectors [par, rot]
        par(arel)         - vector in form of a list pointing to new origin point (OX, OY, OZ)
        rot(ation)         - list containing three angles (in radians) descibing rotation (OX, OY, OZ)  
        """
        par = np.reshape(trans_mat[:, 0], (3,1))
        rot = trans_mat[:, 1]
        self.__obj__= self.__obj__ - par

        return self.rotate(rot, True)
    
    def projection(self):
        """method does z-depth reduction"""

        #ras_v is normalising vector, moves object into camera ndc space (points' xy ranged from 0 to frame_size gonna be visible)
        ras_v = np.array([[__frame_size__/2], [-__frame_size__/2], [0]])
        matrix = self.processing()

        vec_z = matrix[2]
        matrix[0] = matrix[0]/vec_z
        matrix[1] = matrix[1]/vec_z
        return matrix + ras_v

    def rasterization(self):
        """method projects coordinates into xy plane, rasterizes them so that their coordinates are equal to the "pixels" in the terminal"""
        
        #w_size = vector defining window size 
        w_size = self.__wsize__

        #Transforming into ndc space and then into rasterized space
        ndc_v = np.array([__frame_size__, -__frame_size__ , 1])
        ras = np.rint(((self.projection().T)/ndc_v) * w_size.T)

        #Cutting off all points not visible to camera 
        ras_reduced = np.delete(ras, np.where(
            (ras[:, 0] < 0) | (ras[:, 0] >= w_size[0]) | (ras[:, 1] < 0) | (ras[:, 1] >= w_size[1]))[0], axis = 0)
        self.__obj__ = ras_reduced
    
    def processing(self):
        """method adjusts camera view according to window rules"""
        matrix = self.__obj__

        #CHECK IF WORKS FOR MATRIX THAT IS ONLY 1 POINT
        min_vec = np.amin(matrix, 0)
        max_vec = np.amax(matrix, 0)
        
        #concerning z coordiante
        if self.__rules__["adjust"]:
            #adjust means that camera is moved further so the object is fully in front of it
            if min_vec[2] <= 0: matrix = matrix + np.array([[0, 0, min_vec[2] + 1]])
        else:
            matrix = np.delete(matrix, np.where(matrix.T[:,2] <= 0)[0], axis = 1)

        #concerning x,y coordinates
        if self.__rules__["center"]:
            #center means that camera is gonna be moved in XY plane so the object is equally far from every edge
            diff = np.array([0, 0, 0])
            for i in range(2):
                diff[i] = (max_vec[i] - min_vec[i])/2 + min_vec[i]
            matrix = matrix - diff

        return matrix.T
            

    def update_cam(self, trans_mat, obj = None, w_size = None):
        if obj is not None: self.__obj__ = obj
        if w_size is None: w_size = self.__wsize__

        self.__obj__ = self.cs_transform(trans_mat)
        self.__obj__ = self.rasterization(w_size)
