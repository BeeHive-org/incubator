import LCD
import temp

class Main:

    def __init__(self):
        #start LCD object
        self.LCD = LCD.LCD()
        self.tempControl = temp.TempControl()
        