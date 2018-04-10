#model.py
from flask import Flask, render_template

import csv

## model is the only thing that should know where the data is stored

app = Flask(__name__)

BB_FILE_NAME = 'umbball.csv'

FB_FILE_NAME = 'umfootball.csv'


bb_seasons = []
fb_seasons = []

def init_bball(csv_file_name=BB_FILE_NAME):

    with open(BB_FILE_NAME) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global bb_seasons
# bb_seasons = [] # reset, start clean
        ## convert the strings into integers and save them
        bb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            bb_seasons.append(r)



def get_bball_seasons(sortby='year', sortorder='desc'):
    global bb_seasons

    if sortby == 'year':
            sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0
    
    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
##returning the item at index sort col of row
    return bb_seasons


############## getting football ###########

def init_football(csv_file_name=FB_FILE_NAME):

    with open(FB_FILE_NAME) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global fb_seasons
# bb_seasons = [] # reset, start clean
        ## convert the strings into integers and save them
        fb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            fb_seasons.append(r)



def get_football_seasons(sortby='year', sortorder='desc'):
    global fb_seasons

    if sortby == 'year':
            sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0
    
    rev = (sortorder == 'desc')
    sorted_list = sorted(fb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
##returning the item at index sort col of row
    return fb_seasons



