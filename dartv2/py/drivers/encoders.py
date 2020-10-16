import time
import sys
import os

# rear wheels encoders and direction, battery level
# encoders reset

class EncodersIO ():
    def __init__(self, bus_nb = 2, addr = 0x14, sim=False, vsv=None):
        self.__sim = sim
        if self.__sim:
            self.vsv = vsv

        self.__bus_nb = 2
        self.__addr = 0x14 

        # conditional i2c setup
        # if real robot , then we use actual i2c
        # if not , we are on simulated i2c
        if self.__sim:
            import i2csim as i2c
            self.__dev_i2c=i2c.i2c(self.__addr,self.__bus_nb,vsv=self.vsv)
        else:
            import i2creal as i2c
            self.__dev_i2c=i2c.i2c(self.__addr,self.__bus_nb)

        # place your new class variables here

    # place your encoder functions here
