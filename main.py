import cmd
import display
import os

from threading import Thread

def start(auto=False):
	cmd.terminal()

starter = Thread(target=start)
starter.start()

def ren():
	while display.continue_to_render:
		display.render()

Thread(target=ren).start()