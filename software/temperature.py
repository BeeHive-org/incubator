#from machine import Pin
import machine
import onewire
import ds18x20 #library specific for ds18 devices, possibly only for esp32?
import utime
class TempControl:
    def __init__(self):
        #define pins for the H-Bridge (which will be controlling a peltier)
        self.HBPin1 = machine.Pin(5,machine.Pin.OUT)
        self.HBPin2 = machine.Pin(18,machine.Pin.OUT)
        
        #make both pins go low
        self.HBPin1.value(0)
        self.HBPin2.value(0)
        
        #define pin for fan
        self.fanPin = machine.Pin(16,machine.Pin.OUT)
        #turn fan off
        self.fanPin.value(0)

        #define pin for the temperature sensors (DS18B20+)
        # the device is on GPIO22
        # create the onewire object
        self.ow = onewire.OneWire(machine.Pin(22))
        
        self.ds = ds18x20.DS18X20(self.ow)
        #scan devices on bus

        self.roms = self.ds.scan()
        self.temps = [0]*len(self.roms)
        
        print('found devices:', self.roms)
        

        #temperature sensor1
        #temperature sensor2
        #external temperature sensor1
        
        #fan control1

        #turn all pins off

    def read_all_temps(self):
        self.ds.convert_temp()
        self.time_intervals()#always need to wait between reads - this is a playoff between precision and speed.

        for rom in self.roms:
            print(self.ds.read_temp(rom), end=' ')
        print()
        #read temperature from sensors


    def read_temp(self,rom):
        self.ds.convert_temp()
        self.time_intervals()
        print(self.ds.read_temp(rom))


    def goal_temp(self, newTemp):
        if newTemp<self.read_temp(rom=self.roms[0]):
            self.HBPin2.value(0)
            self.HBPin1.value(1)
            self.fanPin.value(1)

        elif newTemp > self.read_temp(rom=self.roms[0]):
            self.HBPin1.value(0)
            self.HBPin2.value(1)
            self.fanPin.value(1)

        else:
            self.HBPin1.value(0)
            self.HBPin2.value(0)
            self.fanPin.value(0)
    
    def time_intervals(self, interval_ms=750):
        time1 = utime.ticks_ms()
        time2 = utime.ticks_ms()
        while time2 - time1 < interval_ms:
            time2 = utime.ticks_ms()