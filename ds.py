#!/usr/bin/python
import sys

class Stack():
	def __init__ (self):
		self.s = []

	def push(self, x):
		self.s.append(x)

	def pop(self):
		return self.s.pop()

	def size(self):
		return len(self.s)

	def show(self):
		print(self.s)
	
	def size(self):
		return len(self.s)
	
	def peek(self):
		return self.s[len(self.s)-1]
