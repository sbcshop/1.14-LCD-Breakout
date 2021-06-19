import random
from machine import Pin, SPI
import st7789
import utime

import vga1_bold_16x32 as font


def main():
    spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
    tft = st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(12, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(13, Pin.OUT),
        rotation=3)

    tft.init()
    utime.sleep(0.5)
    
    tft.text(font,"Hello World!", 0,0)
    #tft.rect(100, 100, 100, 10, st7789.RED)
    tft.fill_rect(70, 40, 120,10, st7789.RED)
    
    
    
main()



