# TMP102 test

from Adafruit_I2C import Adafruit_I2C
import TMP102 as tmp
import time


print 'starting tmp102 test'

t = tmp.TMP102()

while True:
	print t.getTemp()
	time.sleep(0.5)