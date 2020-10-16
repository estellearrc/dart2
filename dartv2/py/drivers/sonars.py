import time
import sys
import os
import platform

class SonarsIO ():
    def __init__(self,sim=False,vsv=None):
        self.__sim = sim
        if self.__sim:
            self.vsv = vsv
        #print ("vsv",vsv,self.vsv)
        self.__bus_nb = 2
        self.__addr_4_sonars = 0x21
        self.__addr_front_left = 0x070
        self.__addr_front_right = 0x072

        # conditional i2c setup
        # if real robot , then we use actual i2c
        # if not , we are on simulated i2c
        if self.__sim:
            import i2csim as i2c
            self.__dev_i2c_4_sonars=i2c.i2c(self.__addr_4_sonars,bus_nb=self.__bus_nb,vsv=self.vsv)
            self.__dev_i2c_front_left=i2c.i2c(self.__addr_front_left,bus_nb=self.__bus_nb,vsv=self.vsv)
            self.__dev_i2c_front_right=i2c.i2c(self.__addr_front_right,bus_nb=self.__bus_nb,vsv=self.vsv)
        else:
            import i2creal as i2c
            self.__dev_i2c_4_sonars=i2c.i2c(self.__addr_4_sonars,self.__bus_nb)
            self.__dev_i2c_front_left=i2c.i2c(self.__addr_front_left,self.__bus_nb)
            self.__dev_i2c_front_right=i2c.i2c(self.__addr_front_right,self.__bus_nb)
            
        # place your new class variables here

    # place your sonar functions here
