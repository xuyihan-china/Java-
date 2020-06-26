#!/bin/env python
# Scott Shawcroft
#
#
#
# This program outputs a ASCII space needle.

SCALE = 3

# Prints the spire section.
def spire():
	for i in range(SCALE):
		print " "*3*SCALE + "||"

# Prints the top section.
def top():
  for i in range(SCALE):
  	print " "*(SCALE-i-1)*3 + "__/" +  ":"*3*i +"||" + ":"*3*i + "\\__"
  print "|" + "\""*SCALE*6 + "|"

# Prints the bottom section.
def bottom():
  for i in range(SCALE):
  	print " "*2*i + "\\_" + "/\\"*(3*SCALE-1-2*i) + "_/"

# Prints the middle section.
def center():
  for i in range(SCALE*SCALE):
  	print " "*(2*SCALE+1) + ("|" + "%"*(SCALE-2) + "|")*2

spire()
top()
bottom()
spire()
center()
top()
