# here's a tiny wrapper for the TMP102 I2C sensor
# AKA MEDIA SYSTEM, 9/2013

from Adafruit_I2C import Adafruit_I2C
import time

class TMP102():
	TMP102_ADDRESS = 0x36

	def __init__(self, *args, **kwargs):
		self.i2c = Adafruit_I2C(self.TMP102_ADDRESS)

	def getTemp(self):
		return self.i2c.read16U(self.TMP102_ADDRESS)
