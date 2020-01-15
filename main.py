from asynchinput import _getChUnix as getCh
from objects import *
from screen import *
import numpy as arraymaker 
import os
import cursor
import time
import signal
from alarmexception import AlarmException
cursor.hide()
sc = screen_renderer()
while True :
    start_time = time.time()
    sc.load_screen()
    p1.moveplayer()
    p1.gravity()
    print("\x1b[%d;%df%s" %(0,0,''))
    p1.display_score()
    sc.render_screen()
    end_time = time.time()
    time.sleep(max(0.1 - (end_time - start_time),0))
