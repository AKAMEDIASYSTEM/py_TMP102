# here's a tiny wrapper for the TMP102 I2C sensor
# AKA MEDIA SYSTEM, 9/2013

from Adafruit_I2C import Adafruit_I2C
import time

class TMP102():
    TMP102_ADDRESS = 0x48 # b1001000 addr pin pulled low
    # TMP102_ADDRESS = 0x49 # b1001001 addr pin pulled high
    # TMP102_ADDRESS = 0x4A b1001010 addr pin tied to SDA
    # TMP102_ADDRESS = 0x4B b1001011 addr pin tied to SCL
    TMP102_WRITE_TO_POINTER = 0x90
    TMP102_READ_FROM_TEMP = 0x00 # write this to the pointer reg to init temp readings
    def __init__(self, *args, **kwargs):
        self.i2c = Adafruit_I2C(self.TMP102_ADDRESS)
        # self.i2c.write8(self.TMP102_WRITE_TO_POINTER, self.TMP102_READ_FROM_TEMP)

    def getTemp(self):
        rd = self.i2c.readU16(self.TMP102_ADDRESS)
        # print 'raw reading is ',rd
        rd = rd >> 4
        # print 'rd is ', rd
        if (rd & (1<<11)):
        	rd |= 0xF800
        	print 'the twos complement thing happened', rd
        result = rd*0.0625
        return result