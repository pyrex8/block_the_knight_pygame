#!/usr/bin/env python
''' 3x5 font http://robey.lag.net/2010/01/23/tiny-monospace-font.html'''

import pygame
from atari import *

# starts at ASCII 32 - space
font_3x5 =  ['   '
            ,'   '
            ,'   '
            ,'   '
            ,'   '

            ,' X '
            ,' X '
            ,' X '
            ,'   '
            ,' X '

			,'X X'
            ,'X X'
            ,'   '
            ,'   '
            ,'   '

			,'X X'
            ,'XXX'
            ,'X X'
            ,'XXX'
            ,'X X'

			,' XX'
            ,'XX '
            ,' XX'
            ,'XX '
            ,' X '

			,'X  '
            ,'  X'
            ,' X '
            ,'X  '
            ,'  X'

			,'XX '
            ,'XX '
            ,'XXX'
            ,'X X'
            ,' XX'

			,' X '
            ,'   '
            ,'   '
            ,'   '
            ,'   '

			,'  X'
            ,' X '
            ,' X '
            ,' X '
            ,'  X'

			,'X  '
            ,' X '
            ,' X '
            ,' X '
            ,'X  '

			,'X X'
            ,' X '
            ,'X X'
            ,'   '
            ,'   '

			,'   '
            ,' X '
            ,'XXX'
            ,' X '
            ,'   '

			,'   '
            ,'   '
            ,'   '
            ,' X '
            ,'X  '

			,'   '
            ,'   '
            ,'XXX'
            ,'   '
            ,'   '

			,'   '
            ,'   '
            ,'   '
            ,'   '
            ,' X '

			,'  X'
            ,'  X'
            ,' X '
            ,'X  '
            ,'X  ']



digits =    ['XXX'
            ,'X X'
            ,'X X'
            ,'X X'
            ,'XXX'

            ,'  X'
            ,'  X'
            ,'  X'
            ,'  X'
            ,'  X'

            ,'XXX'
            ,'  X'
            ,'XXX'
            ,'X  '
            ,'XXX'

            ,'XXX'
            ,'  X'
            ,'XXX'
            ,'  X'
            ,'XXX'

            ,'X X'
            ,'X X'
            ,'XXX'
            ,'  X'
            ,'  X'

            ,'XXX'
            ,'X  '
            ,'XXX'
            ,'  X'
            ,'XXX'

            ,'XXX'
            ,'X  '
            ,'XXX'
            ,'X X'
            ,'XXX'

            ,'XXX'
            ,'  X'
            ,'  X'
            ,'  X'
            ,'  X'

            ,'XXX'
            ,'X X'
            ,'XXX'
            ,'X X'
            ,'XXX'

            ,'XXX'
            ,'X X'
            ,'XXX'
            ,'  X'
            ,'XXX'

			,'   '
            ,' X '
            ,'   '
            ,' X '
            ,'   '

			,'   '
            ,' X '
            ,'   '
            ,' X '
            ,'X  '

			,'  X'
            ,' X '
            ,'X  '
            ,' X '
            ,'  X'            

			,'   '
            ,'XXX'
            ,'   '
            ,'XXX'
            ,'   '

			,'X  '
            ,' X '
            ,'  X'
            ,' X '
            ,'X  '

			,'XXX'
            ,'  X'
            ,' X '
            ,'   '
            ,' X '

			,' X '
            ,'X X'
            ,'XXX'
            ,'X  '
            ,' XX']




upper_c =	[' X '
            ,'X X'
            ,'XXX'
            ,'X X'
            ,'X X'

			,'XX '
            ,'X X'
            ,'XX '
            ,'X X'
            ,'XX '

			,' XX'
            ,'X  '
            ,'X  '
            ,'X  '
            ,' XX'

			,'XX '
            ,'X X'
            ,'X X'
            ,'X X'
            ,'XX '

			,'XXX'
            ,'X  '
            ,'XXX'
            ,'X  '
            ,'XXX'

			,'XXX'
            ,'X  '
            ,'XXX'
            ,'X  '
            ,'X  '

			,' XX'
            ,'X  '
            ,'XXX'
            ,'X X'
            ,' XX'

			,'X X'
            ,'X X'
            ,'XXX'
            ,'X X'
            ,'X X'            

			,'XXX'
            ,' X '
            ,' X '
            ,' X '
            ,'XXX'

			,'  X'
            ,'  X'
            ,'  X'
            ,'X X'
            ,' X '

			,'X X'
            ,'X X'
            ,'XX '
            ,'X X'
            ,'X X'

			,'X  '
            ,'X  '
            ,'X  '
            ,'X  '
            ,'XXX'

			,'X X'
            ,'XXX'
            ,'XXX'
            ,'X X'
            ,'X X'

			,'X X'
            ,'XXX'
            ,'XXX'
            ,'XXX'
            ,'X X'

			,'XXX'
            ,'X X'
            ,'X X'
            ,'X X'
            ,'XXX'

			,'XX '
            ,'X X'
            ,'XX '
            ,'X  '
            ,'X  '

			,' X '
            ,'X X'
            ,'X X'
            ,'X X'
            ,' XX'

			,'XX '
            ,'X X'
            ,'XX '
            ,'XX '
            ,'X X'


			,' XX'
            ,'X  '
            ,' X '
            ,'  X'
            ,'XX '

			,'XXX'
            ,' X '
            ,' X '
            ,' X '
            ,' X '

			,'X X'
            ,'X X'
            ,'X X'
            ,'X X'
            ,' XX'

			,'X X'
            ,'X X'
            ,'X X'
            ,' X '
            ,' X '

			,'X X'
            ,'X X'
            ,'XXX'
            ,'XXX'
            ,'X X'

			,'X X'
            ,'X X'
            ,' X '
            ,'X X'
            ,'X X'

			,'X X'
            ,'X X'
            ,' X '
            ,' X '
            ,' X '

			,'XXX'
            ,'  X'
            ,' X '
            ,'X  '
            ,'XXX'

			,'XXX'
            ,'X  '
            ,'X  '
            ,'X  '
            ,'XXX'

			,'   '
            ,'X  '
            ,' X '
            ,'  X'
            ,'   '

			,'XXX'
            ,'  X'
            ,'  X'
            ,'  X'
            ,'XXX' 

			,' X '
            ,'X X'
            ,'   '
            ,'   '
            ,'   ' 

			,'   '
            ,'   '
            ,'   '
            ,'   '
            ,'XXX' 

			,'X  '
            ,' X '
            ,'   '
            ,'   '
            ,'   ' 
            ]







font_3x5 += digits + upper_c



def place_character(screen, x, y, character, color):
    """Prints a 3x5 font using Playfield pixels, numbers upper case and some 
    special characters"""
    if character < 32 or character > 96:
         character = 63
    character -= 32
    for j in range(5):
        k = font_3x5[(character * 5) + j]
        for i in range(3):
            if k[i] == 'X':
                pygame.draw.line(screen, color
                    , ((x+i)*PF_PIXEL, ((y +j) * PIXEL))
                    , ((x+i)*PF_PIXEL + PF_PIXEL, ((y +j) * PIXEL))
                    , PIXEL)
                playfield_collision((x+i)*4, y + j)

def print_large(self, x, y, pstring, color):
    """Prints a numeric value that is right justified using 3x5 digits in 
    Playfield pixels."""
    for i in range(len(pstring)):
        j = ord(pstring[i])
        place_character(self, x + (i*4), y, j, color)

