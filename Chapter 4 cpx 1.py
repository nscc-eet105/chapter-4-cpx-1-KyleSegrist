# Chapter 4 cpx lab-1
# CPX LED Functions

from adafruit_circuitplayground import cp

WHITE = (20 , 20, 20)
OFF = (0, 0, 0)

def led_pix_on():
    for num in range(0, 10):
        cp.pixels[num] = WHITE


def led_pix_off():
    for num in range(0, 10):
        cp.pixels[num] = OFF


while True:
    if cp.touch_A1:
        led_pix_on()
    else:
        led_pix_off()
# Write your code here :-)
