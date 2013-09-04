# here's a tiny wrapper for the TMP102 I2C sensor
# AKA MEDIA SYSTEM, 9/2013

from Adafruit_I2C import Adafruit_I2C
import time

class TMP102():
	TMP102_ADDRESS = 0x48 # b1001000 addr pin pulled low
	# TMP102_ADDRESS = 0x49 # b1001001 addr pin pulled high
	# TMP102_ADDRESS = 0x4A b1001010 tie to SDA
	# TMP102_ADDRESS = 0x4B b1001011 tie to SCL
	def __init__(self, *args, **kwargs):
		self.i2c = Adafruit_I2C(self.TMP102_ADDRESS)

	def getTemp(self):
		msb = self.i2c.readU8(self.TMP102_ADDRESS)
		print 'msb is ',msb
		lsb = self.i2c.readU8(self.TMP102_ADDRESS)
		print 'lsb is ',lsb
		result = 0.0625*(((msb << 8 ) | lsb) >> 4)
		return result
		# uh, this might be wrong. Might need to 
		# read hi and lo bytes separately to see
		# if we're doing two's complement
