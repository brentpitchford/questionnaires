# -*- coding: utf-8 -*-

# questionnaire.py
# Visual Cognitive Neuroscience Lab
# Brock University
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# This script was developed for use by the Visual Cognitive Neuroscience Lab
# at Brock University.


"""This script...

"""


from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound, monitors

from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import csv

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


# Store info about the experiment session
expName = 'Barretsimpuls'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'01'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
endExpNow = False  # flag for 'escape' or other condition => quit the exp
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename= _thisDir + os.sep + u'BarretsImpuls' + os.sep + '%s_%s' % (expInfo['participant'], expName + ".csv")







####################################################################################################
#                                         Program Constants                                        #
####################################################################################################
# Set psychopy required names for things
EXP_NAME     = "BarrettsScale"  # The name of the experiment for save files
MONITOR_NAME = "testMonitor"     # The name of the monitor set in PsychoPy.


# Set required colours for objects, text, etc
BG_COLOUR     = [-1, -1, -1]  # Set a background colour, currently black
TEXT_COLOUR   = [1, 1, 1]     # The text colour, currently white

# Set required sizes for objects, text, etc
TEXT_HEIGHT   = 1.2       # The height in visual degrees of instruction text
TEXT_WRAP     = 35      # The character limit of each line of text before word wrap

HEADER_LIST = ['Date','Participant', 'Questionnaire' , 'Response' , 'RT']

INS_MSG =    ("\nThe following questions measure some of the ways in which you act and think.\n\n" +
             "Read each statement and " +
             "choose your answer by pressing the appropriate number key "+
             "followed by the enter key.\n\n" +
             " Do not spend too much time on any statement. \n\nAnswer quickly and honestly.\n\n" )


questions_1 = [ 'I plan tasks carefully ', 
               'I do things without thinking ', 
               'I make up my mind quickly ',
               'I am happy-go-lucky ',
               'I dont "pay attention" ',
               'I have "racing" thoughts ', 
               'I plan trips well ahead of time ', 
               'I am self-controlled ',
               'I concentrate easily ',
               'I save regularly ' ,
               'I "squirm" at plays or lectures ' ,
               'I am a careful thinker ' ,
               'I plan for job security ', 
               'I say things without thinking ' ,
               'I like to think about complex problems ', 
               'I change jobs ',
               'I act "on impulse" ', 
               'I get easily bored when solving thought problems ',
               'I act on the spur of the moment ',
               'I am a steady thinker ',
               'I change residences ',
               'I buy things on impulse ',
               'I can only think about one thing at a time ',
               'I change hobbies ',
               'I spend or charge more than I earn ',
               'I often have extraneous thoughts when thinking ',
               'I am more interested in the present than the future ',
               'I am restless at the theater or lectures ',
               'I like puzzles ',
               'I am future-oriented ']
               
def set_psychopy():
    """
    
    """
    
    # Build the monitor with correct sizing for psychopy to calculate visual degrees
    mon = monitors.Monitor('testMonitor')
    mon.setDistance(57)  # Measure first to ensure this is correct
    mon.setWidth(41)     # Measure first to ensure this is correct
    3
    # Build the window for psychopy to run the experiment in
    win = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor=mon, color=BG_COLOUR,
                        colorSpace='rgb', units='deg')
    
    # Set up an event clock for timing in trials
    event_clock = core.Clock()
    
    # Set up an event catcher to collect keyboard and mouse responses
    mouse    = event.Mouse(win=win)
    key_resp = event.BuilderKeyResponse()

    return win, mon, event_clock, key_resp, mouse
# End def set_psychopy
    # Set up an event catcher to collect keyboard and mouse responses


# Setup all required PsychoPy variables
win, mon, event_clock, key_resp, mouse = set_psychopy()

# Build all experiment stimuli
ins  = visual.TextStim(win=win, name='msg', text=INS_MSG, height=1.0, wrapWidth=TEXT_WRAP,
                       color=TEXT_COLOUR, colorSpace='rgb', pos=[0,0])
ans1 = visual.TextStim(win=win, name='msg', text='1 = Not At All', height=0.8, wrapWidth=TEXT_WRAP,
                      color=TEXT_COLOUR, colorSpace='rgb', pos=[-10,-4])
ans2 = visual.TextStim(win=win, name='msg', text='2 = Somewhat', height=0.8, wrapWidth=TEXT_WRAP,
                       color=TEXT_COLOUR, colorSpace='rgb', pos=[-4,-4])
ans3 = visual.TextStim(win=win, name='msg', text='3 = Moderately So', height=0.8, wrapWidth=TEXT_WRAP,
                       color=TEXT_COLOUR, colorSpace='rgb', pos=[4,-4])
ans4 = visual.TextStim(win=win, name='msg', text='4 = Very Much So', height=0.8, wrapWidth=TEXT_WRAP,
                       color=TEXT_COLOUR, colorSpace='rgb', pos=[12,-4])
ans5 = visual.TextStim(win=win, name='msg', text='Skip this question', height=1.0, wrapWidth=TEXT_WRAP,
                       color=TEXT_COLOUR, colorSpace='rgb', pos=[-10,-10])
msg = visual.TextStim(win=win, name='msg', text="", height=1.0, wrapWidth=TEXT_WRAP,
                       color=TEXT_COLOUR, colorSpace='rgb', pos=[0,2])
cls = visual.TextStim(win=win, name='msg', text="Press the enter key to submit your answer", height=1.0, wrapWidth=TEXT_WRAP,
                       color=TEXT_COLOUR, colorSpace='rgb', pos=[10,-10])

# Present instructions for the experiment
ins.setAutoDraw(True)
win.flip()
event.waitKeys()
ins.setAutoDraw(False)
win.flip()

answers_1 = []
for q in questions_1:
    msg.setText(q)
    ans1.setColor([1,1,1])
    ans2.setColor([1,1,1])
    ans3.setColor([1,1,1])
    ans4.setColor([1,1,1])
    ans5.setColor([1,1,1])
    msg.setAutoDraw(True)
    ans1.setAutoDraw(True)
    ans2.setAutoDraw(True)
    ans3.setAutoDraw(True)
    ans4.setAutoDraw(True)
    ans5.setAutoDraw(True)
    win.flip()
    event.clearEvents()
    response = None
    event_clock.reset()
    while True:
        win.flip()
        if event.getKeys(["1"]):
            response = 1
            cls.setAutoDraw(True)
            ans1.setColor([1,-1,-1])
            ans2.setColor([1,1,1])
            ans3.setColor([1,1,1])
            ans4.setColor([1,1,1])
            ans5.setColor([1,1,1])
        elif event.getKeys(["2"]):
            response = 2
            cls.setAutoDraw(True)
            ans1.setColor([1,1,1])
            ans2.setColor([1,-1,-1])
            ans3.setColor([1,1,1])
            ans4.setColor([1,1,1])
            ans5.setColor([1,1,1])
        elif event.getKeys(["3"]):
            response = 3
            cls.setAutoDraw(True)
            ans1.setColor([1,1,1])
            ans2.setColor([1,1,1])
            ans3.setColor([1,-1,-1])
            ans4.setColor([1,1,1])
            ans5.setColor([1,1,1])
        elif event.getKeys(["4"]):
            response = 4
            cls.setAutoDraw(True)
            ans1.setColor([1,1,1])
            ans2.setColor([1,1,1])
            ans3.setColor([1,1,1])
            ans4.setColor([1,-1,-1])
            ans5.setColor([1,1,1])
        elif event.getKeys(["space"]):
            response = 4
            cls.setAutoDraw(True)
            ans1.setColor([1,1,1])
            ans2.setColor([1,1,1])
            ans3.setColor([1,1,1])
            ans4.setColor([1,1,1])
            ans5.setColor([1,-1,-1])
        elif event.getKeys(['enter']) or event.getKeys(['return']):
            if response is not None:
                cls.setAutoDraw(False)
                rt = event_clock.getTime()
                answers_1.append(response)
                break
        elif event.getKeys(["escape"]):
            core.quit(0) # If escape key is hit then safely close program
msg.setAutoDraw(False)
ans1.setAutoDraw(False)
ans2.setAutoDraw(False)
ans3.setAutoDraw(False)
ans4.setAutoDraw(False)
ans5.setAutoDraw(False)
cls.setAutoDraw(False)

#Use this section for scored answers 
#    rev_q = [0, 6, 7, 9, 11, 12, 14, 19, 22, 28]
#    rev   = [1, 2, 3, 4, 5, 8, 10, 13, 15, 16, 17, 18, 20, 21, 23, 24, 25, 26, 27]
#    rev_score =[1,2,3,4]
#
#    scored_answers_1 = []
#    for a in xrange(len(answers_1)):
#        print scored_answers_1
#        if a in rev_q:
#            #scored_answers_1.append(answers_1[a][0])
#            scored_answers_1.append(rev_score[answers_1[a][0]-1])
#        else:
#            scored_answers_1.append(answers_1[a][0])
#            
#            
#            
#    
#    print scored_answers_1



#    rev_q = [0, 6, 7,8,9, 11, 12, 14, 19,28,29]
#    rev   = [4, 3, 2, 1]


#    scored_answers_1 = []
#    for a in xrange(len(answers_1)):
#        if a in rev_q:
#            scored_answers_1.append(rev[answers_1[a]-1])
#        else:
#            scored_answers_1.append(answers_1[a])




# Write output headers to subject save file
with open(filename, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(HEADER_LIST)

if not os.path.exists(filename):
    os.makedirs(filename)

# Open the output file reader for writing
csv_file = open(filename, 'a')
writer   = csv.writer(csv_file)

# Wrtie the answers to file
for x in range(len(answers_1)):
    writer.writerow([expInfo['date'],expInfo['participant'],expInfo['expName'],answers_1[x],rt])
    #writer.writerow([expInfo['date'],expInfo['participant'],expInfo['expName'],answers_1[x], scored_answers_1[x],rt]) 

    
csv_file.flush()
csv_file.close()
# end def run_time
