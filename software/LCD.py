from machine import Pin


class LCD:
    def __init__(self):
        #define I2C pins
        self.dataPin = Pin(13,Pin.output())
        
        #start communication with LCD board
        
