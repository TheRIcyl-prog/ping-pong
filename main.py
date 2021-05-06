from pygame import *

win_width = 1000
win_height = 700
display.set_caption('Ping-Pong')
green = 'green.png'
win = display.set_mode((win_width, win_height))
bg = transform.scale(image.load(green), (1000, 700))


run = True
finish = False

while run:
	for e in event.get():
		if e.type == QUIT:
			run = False

	if not finish:
		win.blit(bg,(0,0))

	display.update()
	time.delay(40)

