"""
handles IO to a sense hat peripheral
"""
from sense_hat import SenseHat
from time import sleep

r = (255,0,0)
g = (0,255,0)
b = (0,0,255)
n = (0,0,0)
l = (255,255,0)

x,y = (1,1)
old = n

border = [
g,n,g,n,g,n,g,n,
n,n,n,n,n,n,n,g,
g,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,g,
g,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,g,
g,n,n,n,n,n,n,n,
n,g,n,g,n,g,n,g
]

sense = SenseHat()

sense.set_pixels(border)

def error(sense):
    for i in range(0, 4):
        sense.clear(r)
        sleep(0.1)
        sense.clear()
        sleep(0.1)

def active_flash(x,y, sense):
    while True:
        sense.set_pixel(x,y, l)
        sense.set_pixel(x, y+1, l)
        sense.set_pixel(x+1, y, l)
        sense.set_pixel(x+1, y+1, l)
        sleep(1.0)
        sense.set_pixel(x,y, n)
        sense.set_pixel(x, y+1, n)
        sense.set_pixel(x+1, y, n)
        sense.set_pixel(x+1, y+1, n)
        sleep(1.0)

while True:
    for event in sense.stick.get_events():
        active_flash(x,y, sense)
        if event.action == 'pressed' and event.direction == 'up':
            if y >= 3:
                y -= 2
        if event.action == 'pressed' and event.direction == 'down':
            if y <= 5:
                y += 2
        if event.action == 'pressed' and event.direction == 'right':
            if x <= 5:
                x += 2
        if event.action == 'pressed' and event.direction == 'left':
            if x >= 3:
                x -= 2
