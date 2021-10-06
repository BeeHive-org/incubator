import LCD
import temperature as temp
import fans

class Main:

    def __init__(self):
        #start LCD object
        self.LCD = LCD.LCD()
        self.tempControl = temp.TempControl()
        self.fans = fans.Fans()
    
    def run_incubator(self,goalTemp = 35):
        while 1:
            self.tempControl.goal_temp(goalTemp)
            self.tempControl.time_intervals()
        