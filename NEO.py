
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
expName = 'NEO'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'01'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
endExpNow = False  # flag for 'escape' or other condition => quit the exp
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename= _thisDir + os.sep + u'NEO' + os.sep + '%s' % (expInfo['participant'] + ".csv")




def run_time(subj_num):
    ####################################################################################################
    #                                         Program Constants                                        #
    ####################################################################################################
    # Set psychopy required names for things
    EXP_NAME     = "NEO"  # The name of the experiment for save files
    MONITOR_NAME = "testMonitor"     # The name of the monitor set in PsychoPy.


    # Set required colours for objects, text, etc
    BG_COLOUR     = [-1,-1,-1]  # Set a background colour, currently black
    TEXT_COLOUR   = [1, 1, 1]     # The text colour, currently white
    TEXT_COLOUR2  = [0, 0, 53]

    # Set required sizes for objects, text, etc
    TEXT_HEIGHT   = 2       # The height in visual degrees of instruction text
    TEXT_WRAP     = 32      # The character limit of each line of text before word wrap
    
    HEADER_LIST = ['Date','Participant', 'Questionnaire' , 'Response' , 'Score', 'RT']

    INS_MSG =    ("\nPlease use the ratings scale to describe how accurately each statement describes you as you are now, not as you wish to be.")

    questions_1 = ['often feel blue ',
'have little to say ',
'believe in the importance of art ',
'have a sharp tongue ',
'am always prepared ',
'rarely get irritated ', 
'feel comfortable around people ',
'am not interested in abstract ideas ',
'have a good word for everyone',
'waste my time',
'dislike myself',
'keep in the background',
'have a vivid imagination',
'cut others to pieces',
'pay attention to details',
'seldom feel blue',
'make friends easily',
'do not like art',
'believe that others have good intentions',
'find it difficult to get down to work',
'am often down in the dumps',
'would describe my experiences as somewhat dull',
'tend to vote for less conservative political candidates',
'suspect hidden motives in others',
'get chores down right away',
'feel comfortable with myself',
'am skilled in handling social situations',
'avoid philosophical discussions',
'respect others',
'do just enough work to get by',
'have frequent mood swings',
'dont like to draw attention to myself',
'carry the conversation to a higher level',
'get back at others',
'carry out my plans',
'am not easily bothered by things',
'am the life of the party',
'do not enjoy going to art musuems',
'accept people as they are',
'dont see things through',
'panic easily',
'dont talk a lot',
'enjoy hearing new ideas',
'insult people',
'make plans and stick to them',
'am very pleased with myself',
'know how to captivate people',
'tend to vote for more conservative political candidates',
'make pople feel at ease',
'avoid my duties']
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
    ans1 = visual.TextStim(win=win, name='msg', text='1 = Very innacurate', height=0.53, wrapWidth=TEXT_WRAP,
                          color=TEXT_COLOUR, colorSpace='rgb', pos=[-13.2,-4])
    ans2 = visual.TextStim(win=win, name='msg', text='2 = Moderately innacurate', height=0.53, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[-7.4,-4])
    ans3 = visual.TextStim(win=win, name='msg', text='3 = Neither accurate nor innacurate ', height=0.52, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[.5,-4])
    ans4 = visual.TextStim(win=win, name='msg', text='4 = Moderately accurate', height=0.53, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[7.9,-4])
    ans5 = visual.TextStim(win=win, name='msg', text='5 = Very accurate', height=0.53, wrapWidth=TEXT_WRAP,
                           color=TEXT_COLOUR, colorSpace='rgb', pos=[13.2,-4])
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
        ans6.setColor([1,1,1])
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
    cls.setAutoDraw(False)

#    rev_q = [0, 4, 6, 12, 14, 17, 21, 23, 25, 26, 29, 35]
#    rev   = [5, 4, 3, 2, 1]

    scored_answers_1 = []
    for a in xrange(len(answers_1)):
#        if a in rev_q:
#            scored_answers_1.append(rev[answers_1[a]-1])
#        else:
            scored_answers_1.append(answers_1[a])

    

    
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
        writer.writerow( [expInfo['date'],expInfo['participant'],expInfo['expName'],answers_1[x], scored_answers_1[x], rt]) 

        
    csv_file.flush()
    csv_file.close()
# end def run_time
    
if __name__ == "__main__":
    run_time(001)

