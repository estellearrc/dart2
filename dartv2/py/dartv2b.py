import drivers.dartv2b_basis
import sys
import time

class DartV2(drivers.dartv2b_basis.DartV2Basis):
    def __init__(self):
        # get init from parent class
        #drivers.dartv2b_basis.DartV2Basis.__init__(self)
        super().__init__()
        # define class variables
        self.myVarDummy = 42

        # place your new class variables here

    # place your new functions here
