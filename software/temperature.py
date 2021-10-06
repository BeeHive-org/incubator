#from machine import Pin
import machine
import onewire
import ds18x20 #library specific for ds18 devices, possibly only for esp32?
import utime
class TempControl:
    def __init__(self,sensorPin = 22,hBrigde1=5,hBridge2=18):
        #define pins for the H-Bridge (which will be controlling a peltier)
        self.HBPin1 = machine.Pin(hBrigde1,machine.Pin.OUT)
        self.HBPin2 = machine.Pin(hBridge2,machine.Pin.OUT)
        
        #make both pins go low
        self.HBPin1.value(0)
        self.HBPin2.value(0)
        
        

        #define pin for the temperature sensors (DS18B20+)
        # the device is on GPIO22
        # create the onewire object
        self.ow = onewire.OneWire(machine.Pin(sensorPin))
        
        self.ds = ds18x20.DS18X20(self.ow)
        #scan devices on bus

        self.roms = self.ds.scan()
        self.temps = [0]*len(self.roms)
        
        print('found devices:', self.roms)
        

        #temperature sensor1
        self.ts1 = self.rom[0]
        #temperature sensor2
        self.ts2 = self.rom[1]

        #external temperature sensor1


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
        if newTemp<self.read_temp(rom=self.ts1):
            self.HBPin1.value(1)
            self.HBPin2.value(0)
            print("temperature lower than goal")

        elif newTemp > self.read_temp(rom=self.ts1):
            self.HBPin1.value(0)
            self.HBPin2.value(1)
            print("temperature higher than goal")
        else:
            self.HBPin1.value(0)
            self.HBPin2.value(0)
            print("temperature just right")
    
    def time_intervals(self, interval_ms=750):
        time1 = utime.ticks_ms()
        time2 = utime.ticks_ms()
        while time2 - time1 < interval_ms:
            time2 = utime.ticks_ms()