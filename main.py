#!/usr/bin/python
# -*- coding: UTF-8 -*-

from datetime import datetime
from flickr2website import flickr2website
import random

DEBUG = True

def randomizer(ODDS):
    if DEBUG==False:
        guess = random.choice(range(ODDS))
    else:
        guess = 0

    if guess != 0:
        print ('randomly skip')
        return 0
    else:
        return 1

    
timezone=3
times={}
times[0]=0
times[1]=0
times[2]=0
times[3]=0
times[4]=0
times[5]=0
times[6]=0
times[7]=0
times[8]=0
times[9]=1
times[10]=0
times[11]=0
times[12]=0
times[13]=0
times[14]=0
times[15]=1
times[16]=0
times[17]=0
times[18]=0
times[19]=0
times[20]=0
times[21]=0
times[22]=0
times[23]=0

#current_hour=15

current_hour=datetime.now().hour


odds=times[current_hour]

if times[current_hour]>0 or DEBUG==True :
    if randomizer(odds) or DEBUG==True:
        
        poster=flickr2website()
        #poster.crawl()
        poster.procedure()
    else:
        pass
else:
    print 'skip by timer'

   