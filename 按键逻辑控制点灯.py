from machine import Pin
import time

led=Pin(0,Pin.OUT)
switch=Pin(1,Pin.IN,Pin.PULL_UP)

while True:
	if switch.value()==0:
		led.value(1)
	else:
		led.value(0)

