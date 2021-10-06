import machine
from shiftregister import ShiftRegister

class Fans():

    def __init__(self):

        self.sr = ShiftRegister()
        self.sr.clear()
        #this system is composed of four fans, belonging to 2 different categories
        #Category1: fans that cool the heat dissipator on the peltier element
        #Category2: fan that circulates air inside the incubator
        
        #address to turn all fans on
        self.allOn  = 0b00001111
        #address to turn all fans off
        self.allOff = 0b00000000
        #sr.clear()

    def fans_on(self):
        self.sr.shift(self.allOn)
        self.sr.shift(b'\xa5')
    
    def fans_off(self):
        self.sr.shift(self.allOff)
        self.sr.shift(b'\xa5')

        


        #all the fans are driven by BeeHive shift register.
        # S0 to S2 are category1 fans
        # S3 is category2 fan