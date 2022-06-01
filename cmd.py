# import requests, random, replit # replit imports for replit-y things

import os
import math
import json

directory = '/root/users/admin/'
real_directory = os.getcwd() + directory
original_directory = directory
tokens = ['cd', 'exit']

exit = False

class cd:
	def split(self):
		self.__iter__ = 0
		self.__split_arr__ = ['']
		for i in range(len(directory)):
			if directory[i] == '/':
				self.__iter__  += 1
				self.__split_arr__.append('')
			else:
				self.__split_arr__[self.__iter__] += directory[i]
		self.__split_arr__.pop(0)
		return self.__split_arr__
	def merge(self, input):
		self.str = '/'
		for i in range(len(input)):
			self.str = self.str + input[i] + '/'
		return self.str
	def back(self):
		if directory == '/root/':
			return '/root/'
		else:
			self.res = self.split()
			self.res = self.res[:-2]
			return self.merge(self.res)
	def change(self, intodir):
		global directory
		self.directory = directory
		self.directory += intodir
		if self.directory[-1] != '/':
			self.directory += '/'
		return self.directory

TT_tokens_valid = ['cd','exit']

class lexer:
	def __init__(self, statement):
		self.statement = statement
	
	def first(self, check, text):
		self.str = ''
		if len(check) > len(text): return 0
		for i in range(len(check)):
			self.str += text[i]
		if self.str == check: return 1
		
		return 0

	def lex(self):
		self.repli = self.statement
		self.repli = self.repli.replace(' ', '')
		self.stat = self.repli
		self.pos = 0
		self.tokens = []
		for i in range(len(self.repli)):
			for j in range(len(tokens)):
				if self.first(tokens[self.search(tokens, tokens[j])], self.stat):
					self.tokens.append(tokens[self.search(tokens, tokens[j])])
					self.stat = self.stat[(len(tokens[j])-1):]

				elif len(self.stat) > 0:
					self.tokens.append(self.stat[0])
			
			self.stat = self.stat[1:]
		self.tokens = self.adjoin(self.tokens, 1)
		return self.tokens

	def search(self, listin, sear):
		self.lis = listin
		self.count = 0
		for i in self.lis:
			if (i == sear):
				return self.count
			self.count += 1
		return False
	
	def adjoin(self, listin, leng):
		self.ad = []
		self.list = listin
		self.curr = ''
		for i in range(len(self.list)):
			if not (len(self.list[i]) > leng):
				self.curr = self.curr + str(self.list[i])
			elif len(self.list[i]) > leng:
				if not self.curr == '': self.ad.append(self.curr)
				self.ad.append(self.list[i])
				self.curr = ''
		self.ad.append(self.curr)
		return self.ad

class parser:
	def __init__(self, input):
		self.input = input

	def read(self, what):
		self.para = False
		if what in self.input:
			self.para = self.input[self.input.index(what) + 1]
			self.para = self.para[1:]
			f = ''
			for i in range(math.floor(len(self.para)/2)):
				f += self.para[i*2]
			self.para = f

			if what == 'cd':
				global directory, exit
				if self.para == '..':
					directory = cd().back()
				else:
					# print(self.para)
					directory = cd().change(self.para)
				return directory
			if self.input[self.input.index(what)] == 'exit':
				exit = True
			# if self.input[self.input.index(what)] == 'pwd':

class terminal:
	def __init__(self):
		global directory
		# response = input(f'{directory} > ')
		# print(parser(lexer(response).lex()).read('cd'))
		# if not exit: self.__init__()

# while True:
	# if not exit:
		# terminal()

# print(parser(lexer('help').lex()).read(TT_tokens_valid))

# helper1 = open(directory + 'data.json',)
# helper = json.load(helper1)
# helper1.close()