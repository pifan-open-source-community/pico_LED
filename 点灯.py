from machine import Pin
import time 

led=Pin(25,Pin.out)

while 1:
	led.high()
	time.sleep(1)
	led.low()
	time.sleep(1)