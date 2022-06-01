import pygame
import os
# import math

pygame.init()
win = pygame.display.Info();

screen = pygame.display.set_mode([win.current_w, win.current_h])
pygame.display.set_caption('VDesk 1.0')

total_frames = 0

class window:
	def draw(self, disp, name='Window', width=50, height=50, background=(255,255,255), x=50, y=50, fullscreen=False):
		font = pygame.font.Font('freesansbold.ttf', 10)
		text = font.render(str(name), True, (255,255,255), None)
		if fullscreen:
			x = 0
			y = 0
			width = win.current_w
			height = win.current_h
		pygame.draw.rect(disp, background, pygame.Rect(x,y,width,height))
		textRect = text.get_rect()
		self.t = textRect
		# textRect.center = (x+width/2, y-10)
		textRect.bottomleft = (x,y)
		disp.blit(text, textRect)

class background:
	def draw(self, disp, path):
		global total_frames
		self.obj = pygame.image.load(os.path.abspath(path))
		self.scale = 1

		dummies = [self.obj.get_width(), self.obj.get_height()]
		filler = True
		while filler:
			if dummies[0] < win.current_w or dummies[1] < win.current_h:
				dummies[0] *= 1.01
				dummies[1] *= 1.01
			elif dummies[0] > win.current_w or dummies[1] > win.current_h:
				dummies[0] *= 0.99
				dummies[1] *= 0.99
			if round(dummies[0]) == win.current_w or round(dummies[1]) == win.current_h:
				dummies[0] = round(dummies[0])
				dummies[1] = round(dummies[1])
				filler = False

		self.obj = pygame.transform.scale(self.obj, (dummies[0], dummies[1]))
		self.offset = ((win.current_w - self.obj.get_width()) / 2, (win.current_h - self.obj.get_height()) / 2)
		disp.blit(self.obj, self.offset)
		del dummies, filler
		return self.obj.get_width()

windows = [
	[window(), screen, (123,50,250), 'Terminal', 100, 100, 'root/']
]
background = background()
pygame_clock = pygame.time.Clock()
continue_to_render = True
mouse_pos = pygame.mouse.get_pos()

def render():
	global total_frames, continue_to_render, mouse_pos
	pygame_clock.tick(0)
	screen.fill((0,0,0))
	background.draw(screen, 'root/bgdefault.png')
	for i in windows:
		i[0].draw(disp=i[1], background=i[2], name=mouse_pos, width=i[4], height=i[5])
	pygame.display.flip()
	# total_frames += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continue_to_render = False
	mouse_pos = pygame.mouse.get_pos()