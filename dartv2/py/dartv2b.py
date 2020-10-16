import drivers.dartv2b_basis
import sys
import time
import numpy as np


def bin2dec(X):
    """
    X is an array
    """
    for i  in range(np.shape(X)[1]):
        if X[0,i] > 32767:
            X[0,i] = X[0,i] -65536
    return X




class DartV2(drivers.dartv2b_basis.DartV2Basis):
    def __init__(self):
        # get init from parent class
        #drivers.dartv2b_basis.DartV2Basis.__init__(self)
        super().__init__()
        # define class variables
        self.myVarDummy = 42
    
    def delta_front_odometers(self,dt):
        """
        return diff encoder wheel between dt
        """
        nb_ticks1 = np.array([self.get_front_encoders()])
        time.sleep(dt)
        nb_ticks2 = np.array([self.get_front_encoders()])
        conv_nb_ticks1 = bin2dec(nb_ticks1)
        conv_nb_ticks2 = bin2dec(nb_ticks2)
        diff = conv_nb_ticks2 - conv_nb_ticks1
        return diff

    
        # place your new class variables here

    # place your new functions here

