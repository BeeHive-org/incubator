import machine

#literal code from https://forum.micropython.org/viewtopic.php?t=1219#

class ShiftRegister:
    def __init__(self,srclk=22,srclr=23,serIn=19,rclk=21):
        self.srclk = machine.Pin(srclk,machine.Pin.OUT)
        self.srclr = machine.Pin(srclr,machine.Pin.OUT)
        self.serIn = machine.Pin(serIn,machine.Pin.OUT)
        self.rclk = machine.Pin(rclk,machine.Pin.OUT)
        spi = machine.SPI(1, baudrate=1000000,
                          sck=self.srclk, mosi=self.serIn)
        spi.write(b'\xff')
        self.spi = spi 
        #self.rclk = rclk
        #self.oe = oe
        #self.clr = clr 
        #self.oe.value(0) # output enable
        self.srclr.value(1) # don't reset shift regs

    def clear(self):
        self.srclr.value(0) # clear shift regs
        self.rclk.value(1) # latch data to output
        self.rclk.value(0)
        self.srclr.value(1)

    def shift(self, buf):
        self.spi.write(buf)
        self.rclk.value(1) # latch data to output
        self.rclk.value(0)


#usage: 

#from machine import Pin, softSPI

## create SPI bus and pin objects
#spi = SoftSPI(baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None)
# spi = SPI(1, baudrate=1000000, polarity=0, phase=0) # right now this is hard SPI library.
#spi.write(b'\xff')
#rclk = Pin('X3', Pin.OUT_PP)
#oe = Pin('X2', Pin.OUT_PP)
#clr = Pin('X1', Pin.OUT_PP)
#sr = ShiftRegister(spi, rclk, oe, clr)

# use the shift register
#sr.clear()
#sr.shift(0b01010101)
#sr.shift(b'\xa5')
