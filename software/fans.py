import machine
from shiftregister import ShiftRegister

class Fans():

    def __init__(self):

        self.sr = ShiftRegister()
        
    #this system is composed of four fans, belonging to 2 different categories
        #Category1: fans that cool the heat dissipator on the peltier element
        #Category2: fan that circulates air inside the incubator

        #all the fans are driven by BeeHive shift register.
        # S0 to S2 are category1 fans
        # S3 is category2 fan