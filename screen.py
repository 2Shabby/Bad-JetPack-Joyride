import numpy as arraymaker 
import random
from objects import *
class screen_renderer:
    def __init__(self):
        self.to_be_gen = 0
        self.x = 0
        self.y = 0
    def load_screen(self):
        for i in range(0,SCREEN_HEIGHT-1):
            for j in range(0,SCREEN_WIDTH-1):
                renderer[i][j] = board[i][j+1]
                board[i][j] = board[i][j+1]
                if renderer[i][j] == 'M':
                   p1.attract_player(j,i)
        generate_last = random.choice([1,2,3])
        board[0][SCREEN_WIDTH-1]='_'
        board[SCREEN_HEIGHT-1][SCREEN_WIDTH-1]='_'
        for i in range(1,SCREEN_HEIGHT-1):
            board[i][SCREEN_WIDTH-1]=' '
        if self.to_be_gen != 0:
            if self.to_be_gen == 1:
                board[self.y][SCREEN_WIDTH-1]=laser_one[0]
                self.to_be_gen = 11
            elif self.to_be_gen == 11:
                board[self.y][SCREEN_WIDTH-1]=laser_one[0]
                self.to_be_gen = 0
                self.y = self.y-1
            elif self.to_be_gen == 3:
                board[self.y][SCREEN_WIDTH-1]=laser_three[0]
                self.to_be_gen = 33
                self.y = self.y-1
            elif self.to_be_gen == 33:
                board[self.y][SCREEN_WIDTH-1]=laser_three[0]
                self.y = 0
                self.to_be_gen = 0
        else:
            if generate_last == 1:
                for i in range(1,SCREEN_HEIGHT-1):
                    iscoin = random.randrange(1,20,1)
                    if iscoin == 1:
                        board[i][SCREEN_WIDTH-1]='1'
            elif generate_last == 2:
                ismagnet = random.randrange(1,30,1)
                if ismagnet == 1:
                    y_coord = random.randrange(1,GROUND_LEVEL,1)
                    board[y_coord][SCREEN_WIDTH-1]='M'
            elif generate_last==3:
                islaser = random.randrange(0,10,1)
                if islaser == 1:
                    type_of_laser=random.randrange(1,4,1)
                    if type_of_laser == 1:
                        y_coord = random.randrange(1,SCREEN_HEIGHT-3,1)
                        board[y_coord][SCREEN_WIDTH-1]=laser_one[0]
                        self.y = y_coord
                        self.to_be_gen = 1
                    elif type_of_laser==3:
                        y_coord = random.randrange(3,SCREEN_HEIGHT-1,1)
                        self.y = y_coord
                        self.to_be_gen=3
                        board[y_coord][SCREEN_WIDTH-1]=laser_three[0]
                        self.y = self.y - 1
                    elif type_of_laser ==2:
                        y_coord = random.randrange(3,SCREEN_HEIGHT-1,1)
                        board[y_coord-1][SCREEN_WIDTH-1]=laser_two[0]
                        board[y_coord-2][SCREEN_WIDTH-1]=laser_two[0]
                        board[y_coord][SCREEN_WIDTH-1]=laser_two[0]
        for i in range(1,SCREEN_HEIGHT-1):
            renderer[i][SCREEN_WIDTH-1]=board[i][SCREEN_WIDTH-1]
    def render_screen(self):
        for i in range(0,SCREEN_HEIGHT):
            for j in range(0,SCREEN_WIDTH):
                print(renderer[i][j],end='')
            print('',end='\n')
