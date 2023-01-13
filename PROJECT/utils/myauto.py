import random
from re import T
import time
import pyautogui as pyauto
import sys
from . import mySetting

# pipが必要なもの
# pyautogui, openCV, pillow

def click(x,y,randScope = 50):
    sleeptime = random.randint(1,500)/1000
    # ////////////////////////////////////

def waitClickable(fileName, maxCount = 101, raiseExceptionFlag = False):
    waitCount = 0
    while pyauto.locateOnScreen(fileName , confidence=0.8) is None:
        time.sleep(0.1)
        waitCount = waitCount + 1

        # ////////////////////////////////////
    
    return True

def waitClickableLong(fileName, maxCount = 201, sleepTime = 5):
    waitCount = 0
    freezeCount = 0
    while pyauto.locateOnScreen(fileName , confidence=0.8) is None:
        time.sleep(sleepTime)
        # ////////////////////////////////////
    
    return True

def waitBattleFinish(maxCount = 201):
    waitCount = 0
    freezeCount = 0
    # ////////////////////////////////////

    return True

def waitNotClickable(fileName, customConfidence = 0.8, maxCount = 101):
    waitCount = 0
    # ////////////////////////////////////
    
    return True

def targetClick(fileName, fluctuation = 10, waitCount = 101):
    waitClickable(fileName, waitCount)
    x1,y1 = pyauto.locateCenterOnScreen(fileName , confidence=0.8)
    click(x1,y1,fluctuation)