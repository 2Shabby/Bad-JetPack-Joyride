from asynchinput import _getChUnix as getCh
from sprites import *
import numpy as arraymaker 
import os
import cursor
import time
import signal
from alarmexception import AlarmException
b = ['_']
a = [' ']
a = a*40
b = b*40
bullet_coord = [0]
bullet_coord = bullet_coord * 10
board = arraymaker.array([b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b]);
renderer = arraymaker.array([b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,b]);
GROUND_LEVEL = 14
GRAVITY_ACCEL = 1
FORWARD_SPEED = 2
BACKWARD_SPEED = 2
UPWARD_SPEED = 2
SCREEN_WIDTH = 40
SCREEN_HEIGHT = 18
SCREEN_MOVEMENT_SPEED = 1
ATTRACT_FORCE = 1
SHEILD_ACTIVE = 0
SHEILD_START  = time.time()
class characters:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.player_score=0
        self.lives = 3
        self.sheild = 0
        self.sheild_time = time.time()
        self.bullet_no = 0
        self.bullet_x = arraymaker.array(bullet_coord)
        self.bullet_y = arraymaker.array(bullet_coord)
class player(characters):
    def moveplayer(self):
        def alarmhandler(signum,frame):
            raise AlarmException
        def user_input(timeout=0.1):
                ''' input method '''
                signal.signal(signal.SIGALRM, alarmhandler)
                signal.setitimer(signal.ITIMER_REAL, timeout)
                try:
                    text = getCh()()
                    signal.alarm(0)
                    return text
                except AlarmException:
                    pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''
        c = user_input()
        if c == 'a':
            self.x = max(0,self.x - BACKWARD_SPEED)
        elif c == 'd':
            self.x = min(self.x + FORWARD_SPEED,SCREEN_WIDTH-2)
        elif c == 'w':
            self.y = max(1,self.y - UPWARD_SPEED)
        elif c == 'q':
            exit()
        elif c == 's':
            self.sheild = 1
            self.sheild_time = time.time()
        elif c == 'p':
            self.bullet_x[self.bullet_no]=self.x+1
            self.bullet_y[self.bullet_no]=self.y
            self.bullet_no = (self.bullet_no + 1)%10
        for i in range(0,self.bullet_no):
            if self.bullet_x[i] > SCREEN_WIDTH-2:
                self.bullet_x[i] = -1
            if self.bullet_x[i]!=-1:
                self.bullet_x[i]=self.bullet_x[i]+1
                if renderer[self.bullet_y[i]][self.bullet_x[i]] in ['|','/','-']:
                    board[self.bullet_y[i]][self.bullet_x[i]] = ' '
                    self.bullet_x[i]=-1
                else:
                    renderer[self.bullet_y[i]][self.bullet_x[i]] = 'B'
        for i in range(0,len(player_sprite)):
            for j in range(0,len(player_sprite[i])):
                    if renderer[self.y+i][self.x+j]=='1':
                        self.player_score = self.player_score + 1
                        board[self.y+i][self.x+j]=' '
                    if (renderer[self.y+i][self.x+j]=='/' or renderer[self.y+i][self.x+j]=='|' or renderer[self.y+i][self.x+j]=='-') and self.sheild == 0:
                        self.lives = self.lives - 1
                        self.sheild = 1
                        self.sheild_time = time.time()
                    if (time.time() - self.sheild_time) > 10:
                        self.sheild = 0
                    renderer[self.y+i][self.x+j]=player_sprite[i][j]
    def attract_player(self,x,y):
        if x > self.x :
            self.x = min(self.x + ATTRACT_FORCE,SCREEN_WIDTH-2)
        elif x < self.x:
            self.x = self.x - ATTRACT_FORCE
        if y > self.y:
            self.y = min(self.y + ATTRACT_FORCE,GROUND_LEVEL)
        elif y < self.y:
            self.y = self.y - ATTRACT_FORCE
            print(y-self.y)
    def gravity(self):
        self.y = min(self.y + GRAVITY_ACCEL,GROUND_LEVEL); 
    def display_score(self):
        print(self.player_score)
        print(self.lives)
p1 = player(1,1)
