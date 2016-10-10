#! /usr/bin/env python
""" pyweek 22 entry 'You can't let him in here.""" 

__author__ = "Rex Allison"
__copyright__ = "Copyright 2016, Rex Allison"
__license__ = "MIT"

from atari import *
from font import *
from nemesis import *
from level import *
import math 



# all playfeild and player data here

NUM_LEVELS = 30

sound_type = 0
freq_number = 0
sound_number = 1

anamation = 0.0

nemesis_y = 42.0
direction1 = -1.0
fire = 0
fire_x = 0
fire_y = 0
fire_v = 0

retries = 0
level_number = 1
field_width = 12


t = 0
pos_x = 4
pos_y = (SCREEN_Y/2 + field_width) * 50
vel_x = 0
vel_y = 0
height0 = 4
direction0 = -1.0

jumping = 0 


color_p0 = 2 + (8 * 3)
color_p1 = 1 + (8 * 5)
color_pf = 3 + (8 * 7)
color_bk1 = 0 + (8 * 1)
color_bk2 = 7 + (8 * 1)

blocky = []

blocky =  ['XXXX    '
          ,'XXXX    '
          ,'XXXX    '
          ,'XXXX    ']
       


pf_left =   []
pf_right =  []

for i in range(len(level)):


    w = str(level[i])
    firstpart = str(w[:20])
    secondpart = str(w[20:])
    pf_left.append( firstpart )
    pf_right.append( secondpart )

# end data
game_title('Block the Knight')
move = ''

while move != 'quit':
    dt = clock.tick(FRAME_RATE)

    reset_collision()
    background(screen, 0, WINDOWHEIGHT, colors_hex[color_bk1])
    background(screen, SCREEN_Y/2 - field_width, 2* field_width
        , colors_hex[color_bk2])

    anamation += dt/100.0
    if anamation >= 2.0:
        anamation = 0.0

    d = int(fire_x/50)

    if level_number < NUM_LEVELS and vel_x > 0: 
        nemesis_y += direction1 * dt/100.0 
        missile1(screen, d, fire_y + 6, 1, 1, colors_hex[color_p1])

    pos_x +=  vel_x * dt/50.0
    pos_y += vel_y * dt/50.0

    if pos_y > (SCREEN_Y/2 + field_width) * 50:
        vel_y = 0
        pos_y = (SCREEN_Y/2 + field_width) * 50
        jumping = 0
        direction0 = -1.0

    if pos_y < (SCREEN_Y/2 - field_width + height0) * 50:
        vel_y = 0
        pos_y = (SCREEN_Y/2 - field_width + height0)*50
        jumping = 0
        direction0 = 1.0

    if pos_x > (SCREEN_X + 7)*50:
        level_number += 1
        if level_number > NUM_LEVELS:
            level_number = NUM_LEVELS
        pos_x = 0
        pos_y = (SCREEN_Y/2 + field_width)*50
        jumping = 0
        direction0 = -1.0
        color_p0 = (color_p0 + 8) & 0x7F
        color_p1 = (color_p1 + 8) & 0x7F 
        color_pf = (color_pf + 8) & 0x7F
        color_bk1 = (color_bk1 + 8) & 0x7F
        color_bk2 = (color_bk2 + 8) & 0x7F
        fire = 0


    if level_number == NUM_LEVELS:
        pos_x = (SCREEN_X- 14)*50
        pos_y = (SCREEN_Y/2 + 2) * 50
    player0(screen, int(pos_x/50), int(pos_y/50)-4, blocky, colors_hex[color_p0])

    a = int(anamation)
    b = level_number - 1
    c = int(nemesis_y)
    for i in range(6):
        playfield(screen, 40 + 4*i, 4, pf_left[i+6*b], colors_hex[color_pf], 1, 0)
        playfield(screen, 40 + 4*i, 4, pf_right[i+6*b], colors_hex[color_pf]
            , 0, 1)

    if direction1 < 0:
        missile0(screen, 152, SCREEN_Y/2 - field_width - 1, 8, 1, colors_hex[color_p0]) 
    else:
        missile0(screen, 152, SCREEN_Y/2 + field_width, 8, 1, colors_hex[color_p0])    

    if fire == 0:
        fire = 1
        fire_x = 152 * 50
        fire_y = c
        fire_v = -120
    else:
        fire_x += fire_v*dt/50.0

    if fire_x < 0:
        fire_x = 0
        fire = 0


    player1(screen, 152, c, nemesis[(b*24)+(a*12):(b*24)+(a*12)+12]
        , colors_hex[color_p1])


    if retries > 999:
        retries = 999

    number(screen, 9, 2, retries, colors_hex[color_p0])
    number(screen, 24, 2, level_number, colors_hex[color_p0])

    print_large(screen, 28, 2, '-30', colors_hex[color_p0])
    
    move = update_switches()
        
    # Start screen
    if vel_x == 0 and level_number == 1:
        vel_x = 0
        vel_y = 0
        pos_x = 0 
        pos_y = (SCREEN_Y/2 + field_width) * 50 
        print_large(screen, 2, 97-24, ' TO START', colors_hex[color_p0])
        print_large(screen, 2, 97-16, '  PRESS', colors_hex[color_p0])
        print_large(screen, 2, 97-8, 'SPACE BAR', colors_hex[color_p0])

    # End SCREEN
    if level_number == NUM_LEVELS:
        vel_x = 0
        vel_y = 0
        pos_x = 0
        pos_y = (SCREEN_Y/2 + field_width) * 50    
        print_large(screen, 2, 2+16, '   YOU', colors_hex[color_p0])
        print_large(screen, 2, 2+24,  ' DID IT!', colors_hex[color_p0])

        print_large(screen, 2, 97-24, ' PRESS F', colors_hex[color_p0])
        print_large(screen, 2, 97-16,  ' TO PLAY', colors_hex[color_p0])
        print_large(screen, 2, 97-8,    '  AGAIN', colors_hex[color_p0])

    if get_collision(P0, P1):
        sound (8, 15, 8, 1024)
        retries += 1
        vel_y = 0
        pos_x = 0
        pos_y = (SCREEN_Y/2 + field_width) * 50
        jumping = 0
        direction0 = -1.0
        fire = 0

    if get_collision(P0, M1):
        sound (8, 15, 8, 1024)
        retries += 1
        vel_y = 0
        pos_x = 0
        pos_y = (SCREEN_Y/2 + field_width) * 50
        jumping = 0
        direction0 = -1.0
        fire = 0

    if get_collision(M1, PF):
        fire = 0

    if get_collision(P0, PF):
        sound (8, 15, 8, 1024)
        retries += 1
        vel_y = 0
        pos_x = 0
        pos_y = (SCREEN_Y/2 + field_width) * 50
        jumping = 0
        direction0 = -1.0
        fire = 0

    if get_collision(P1, M0):
        direction1 = -direction1

    if move == 'fire0':
        if vel_x > 0:
            if jumping == 0:
                sound (8, 15, 4, 1024)
                jumping = 1
                vel_y = 180 * direction0
        else:
            vel_x = 240


    if move == 'fire1':
        if vel_x == 0:
            level_number = 1            
            anamation = 0.0
            nemesis_y = 42.0
            direction1 = -1.0
            fire = 0
            fire_x = 0
            fire_y = 0
            fire_v = 0
            retries = 0

    if move == 'up1':
        if level_number < NUM_LEVELS:
            level_number += 1

    if move == 'down1':
        if level_number > 0:
            level_number -= 1



    # Game code ends here
    pygame.display.flip()
    clock.tick(40)

stream.close()
p.terminate()    
pygame.quit()
