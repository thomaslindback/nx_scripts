from gpiozero import LED
from time import sleep

def toggle(port):
    led = LED(port)
    led.on()
    sleep(0.1)
    led.off()
