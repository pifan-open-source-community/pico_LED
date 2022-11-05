from machine import Pin
import time

led=Pin(0,Pin.OUT)
switch=Pin(1,Pin.IN,Pin.PULL_UP)
led.off()


def on_led(switch):
    led.on()
    time.sleep(5)
    led.off()

    

switch.irq(on_led,Pin.IRQ_FALLING)

