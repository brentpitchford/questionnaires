
# -*- coding: utf-8 -*-

# questionnaire.py
# Visual Cognitive Neuroscience Lab
# Brock University
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# This script was developed for use by the Visual Cognitive Neuroscience Lab
# at Brock University.
# Modified by Brent Pitchford <bp11lj@brocku.ca> Oct. 28/2016 for Attention Lab

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
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)


# Store info about the experiment session
expName = 'Circumplex'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'01'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
endExpNow = False  # flag for 'escape' or other condition => quit the exp
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename= _thisDir + os.sep + u'Circumplex' + os.sep + '%s' % (expInfo['participant'] + ".csv")




def run_time(subj_num):
    ####################################################################################################
    #                                         Program Constants                                        #
    ####################################################################################################
    # Set psychopy required names for things
    EXP_NAME     = "Circumplex"  # The name of the experiment for save files
    MONITOR_NAME = "testMonitor"     # The name of the monitor set in PsychoPy.


    # Set required colours for objects, text, etc
    BG_COLOUR     = [-1,-1,-1]  # Set a background colour, currently black
    TEXT_COLOUR   = [1, 1, 1]     # The text colour, currently white
    TEXT_COLOUR2  = [0, 0, 53]

    # Set required sizes for objects, text, etc
    TEXT_HEIGHT   = 2       # The height in visual degrees of instruction text
    TEXT_WRAP     = 32      # The character limit of each line of text before word wrap
    
    HEADER_LIST = ['Date','Participant', 'Questionnaire' , 'Response' , 'Score', 'RT']

    INS_MSG =    ("\nThere will be phrases describing people's behaviors. Please use the rating scale below the questions to describe how accurately each statement describes you. \n\n" +
                 "Describe yourself as you generally are now, not as you wish to be in the future.\n\n" +
                 "So that you can describe yourself in an honest manner, your responses will be kept in absolute confidence. " +
                 "Please read each statement carefully, and then choose the response number which best corresponds with your behaviour.")

    questions_1 = ['At this moment, I feel nervous ',
'For some reason,I feel scared and afraid ',
'For some reason, Ive been feeling sort of nervous ',
'I am feeling "unruffled." ',
'I am feeling quiet ',
'I am feeling troubled ', 
'I feel comfortable and content ',
'I feel content ',
'I feel determined ',
'Right now, I am sharp and attentive ',
'Right now, life feels like one big struggle ',
'Right now, life feels terrific ',
'Things are dull and boring ',
'Things feel pretty dull right now ',
'I feel disturbed and upset ',
'I feel droopy and drowsy ',
'I feel ecstatic ',
'I feel enthusiastic ',
'I feel exhausted ',
'I feel guilty about something that I have said or done ',
'I feel interested in what I am doing at the moment ',
'I feel iritated by something ',
'I feel jittery ',
'I feel on edge ',
'I feel peaceful ',
'I feel pleasantly at rest ',
'I feel powerful and strong ',
'I feel pretty enthusiastic about my life right now ',
'I feel proud of myself ',
'I feel rather distressed ',
'I feel set and determined about something right now ',
'I feel sluggish and slow ',
'Im feeling inspired ',
'Im feeling lively and cheerful ',
'Im feeling placid, low in energy ',
'I am full of guilt and remorse ',
'I am happy ',
'I am satisfied ',
'I am stirred up ',
'I am unhappy ',
'I feel alive and active ',
'l feel angry ',
'I feel ashamed of myself',
'l feel at ease ',
'I feel calm and relaxed ',
'I feel calm, cool, and collected ',
'Im feeling pleasantly well-rested ',
'Im feeling pretty angry at the moment ',
'Im feeling sluggish and dragged out ',
'Im feeling stirred up ',
'Im feeling untroubled and comfortable ',
'Im filled with energy ',
'Im full of energy and tension ',
'Im having some trouble paying attention ',
'Im keyed up ',
'Im too relaxed to worry about anything ',
'My body feels activated ',
'My body feels still ',
'My body is in a quiet, still state ',
'I feel tired ',
'I feel unhappy ',
'I feel very focused and on task ',
'I feel very inspired ',
'I feel worried ',
'I have little interest in things around me ',
'Im bothered by something ',
'Im dissatisfied ',
'Im exhausted ',
'Im feeling energetic and positive ',
'My internal engine is running slow and smoothly ',
'My mind and body are resting, near sleep ',
'My mood is not good ',
'My mood is positive ',
'Overall, I am satisfied ',
'Right now, everything feels dull and boring ',
'Right now, I am at ease with things ',
'Im miserable ']
    def set_psychopy():
        """
        
        """
        
        # Build the monitor with correct sizing for psychopy to calculate visual degrees
        mon = monitors.Monitor('testMonitor')
        mon.setDistance(55)  # Measure first to ensure this is correct
        mon.setWidth(32)     # Measure first to ensure this is correct
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

    # Setup all required PsychoPy variables
    win, mon, event_clock, key_resp, mouse = set_psychopy()

    # Build all experiment stimuli
    ins  = visual.TextStim(win=win, name='msg', text=INS_MSG, height=1.0, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[0,0])
    ans1 = visual.TextStim(win=win, name='msg', text='1 = Not At All', height=0.8, wrapWidth=TEXT_WRAP,
                          color=TEXT_COLOUR, colorSpace='rgb', pos=[-12,-4])
    ans2 = visual.TextStim(win=win, name='msg', text='2', height=0.8, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[-7,-4])
    ans3 = visual.TextStim(win=win, name='msg', text='3 ', height=0.8, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[-2,-4])
    ans4 = visual.TextStim(win=win, name='msg', text='4', height=0.8, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[3,-4])
    ans5 = visual.TextStim(win=win, name='msg', text='5 = Very Much So', height=0.8, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[10,-4])
    ans6 = visual.TextStim(win=win, name='msg', text='Skip this question', height=1.0, wrapWidth=TEXT_WRAP,
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
        ans6.setAutoDraw(True)
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
                ans6.setColor([1,1,1])
            elif event.getKeys(["2"]):
                response = 2
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,-1,-1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,1,1])
                ans6.setColor([1,1,1])
            elif event.getKeys(["3"]):
                response = 3
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,-1,-1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,1,1])
                ans6.setColor([1,1,1])
            elif event.getKeys(["4"]):
                response = 4
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,-1,-1])
                ans5.setColor([1,1,1])
                ans6.setColor([1,1,1])
            elif event.getKeys(["5"]):
                response = 5
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,-1,-1])
                ans6.setColor([1,1,1])
            elif event.getKeys(["space"]):
                response = 999
                cls.setAutoDraw(True)
                ans1.setColor([1,1,1])
                ans2.setColor([1,1,1])
                ans3.setColor([1,1,1])
                ans4.setColor([1,1,1])
                ans5.setColor([1,1,1])
                ans6.setColor([1,-1,-1])
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
    ans6.setAutoDraw(False)
    cls.setAutoDraw(False)

#    rev_q = [0, 4, 6, 12, 14, 17, 21, 23, 25, 26, 29, 35]
#    rev   = [5, 4, 3, 2, 1]

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
    for x in xrange(len(answers_1)):
        writer.writerow( [expInfo['date'],expInfo['participant'],expInfo['expName'],answers_1[x], rt]) 

        
    csv_file.flush()
    csv_file.close()
# end def run_time
    
if __name__ == "__main__":
    run_time(001)

