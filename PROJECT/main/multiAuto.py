import time
import pyautogui as pyauto
import random
import sys
import pyperclip

sys.path.append('../')
from workspace.utils import myauto
from workspace.utils import mySetting
from workspace.utils import twitterApiv2 as api

def reload():
    # リロード
    pyauto.hotkey('alt','f')
    myauto.waitClickable(mySetting.PICTURE_SETTING)
    pyauto.typewrite('bm')

def multiLimit3():
    myauto.targetClick(mySetting.PICTURE_GOTO_MYPAGE)
    reload()
    myauto.targetClick(mySetting.PICTURE_JOIN_NOW)
    # wait
    myauto.fullAutoClick()
    myauto.waitBattleFinish()
    reload()

myauto.click(320,200)

# exeNum = random.randint(3,10)
exeNum = 100
waveCount = 1
params1 = mySetting.anima
summon = mySetting.PICTURE_ZEUS
print(str(exeNum) + '実行します')

reload()

for _ in range(exeNum):
    
    rdInt = random.randint(1,1000)/1000
    time.sleep(rdInt)

    myauto.targetClick(mySetting.PICTURE_INPUTID,5)
    time.sleep(rdInt)
    myauto.targetClick(mySetting.PICTURE_TEXTBOX)
    pyperclip.copy(api.getTweetByText(params1))
    pyauto.hotkey('ctrl','v')
    myauto.targetClick(mySetting.PICTURE_JOIN)

    try:
        myauto.waitClickable(mySetting.PICTURE_SUPPORTER,maxCount = random.randint(20,30), raiseExceptionFlag = True)
    except:
        print('catch')
        if pyauto.locateOnScreen(mySetting.PICTURE_JOINLIMIT2, confidence=0.8):
            print('参加上限1')
            myauto.targetClick(mySetting.PICTURE_GOTO_MYPAGE)
            time.sleep(1)
            reload()
            continue
        elif pyauto.locateOnScreen(mySetting.PICTURE_JOINLIMIT3, confidence=0.8):
            print('参加上限3')
            myauto.targetClick(mySetting.PICTURE_GOTO_MYPAGE)
            time.sleep(1)
            multiLimit3()
            continue
        elif pyauto.locateOnScreen(mySetting.PICTURE_FINISHED_MULTI, confidence=0.8):
            print('終了しているマルチ')
            myauto.targetClick(mySetting.PICTURE_GOTO_MYPAGE)
            time.sleep(1)
            reload()
            continue
        elif pyauto.locateOnScreen(mySetting.PICTURE_CHECK_RESULT, confidence=0.8):
            print('リザルト確認')
            myauto.targetClick(mySetting.PICTURE_OK2)
            time.sleep(rdInt)
            while pyauto.locateOnScreen(mySetting.PICTURE_GET_REWARD_MULTI , confidence=0.8):
                myauto.targetClick(mySetting.PICTURE_GET_REWARD_MULTI)
                time.sleep(rdInt)
                myauto.targetClick(mySetting.PICTURE_BACK)
                time.sleep(rdInt)
                time.sleep(0.5)
            time.sleep(1)
            reload()
            continue
        else:
            sys.exit()

    myauto.targetClick(summon)
    time.sleep(rdInt)

    myauto.targetClick(mySetting.PICTURE_OK_SUMMON)

    time.sleep(0.1)
    if pyauto.locateOnScreen(mySetting.PICTURE_FINISHED_MULTI, confidence=0.8):
        print('終了マルチ')
        myauto.targetClick(mySetting.PICTURE_GOTO_MYPAGE)
        time.sleep(1)
        reload()
        continue
    
    # マウスカーソル退避
    pyauto.move(-300 + rdInt/5 , -100 - rdInt/5)
    
    # 最終Waveまで攻撃リロード
    for wave in range(waveCount):
        throughFlg = False
        joinLimitFlg = False

        # wait
        myauto.waitClickable(mySetting.PICTURE_ATTACK)
        throughFlg = False

        # ここから戦闘
        if throughFlg == False:
            # # 攻撃ボタンクリック       
            myauto.targetClick(mySetting.PICTURE_QUICKSUMMON)
            # # time.sleep(10)
            # time.sleep(rdInt)

            # 3chara
            myauto.charaClick(3)
            myauto.abilityClick(1)
            myauto.abilityClick(2)
            myauto.abilityClick(3)
            time.sleep(rdInt)

            # 4chara
            myauto.targetClick(mySetting.PICTURE_RIGHTCHARA,5)
            myauto.abilityClick(1)
            myauto.abilityClick(2)
            myauto.abilityClick(3)
            time.sleep(rdInt)

            # 4chara
            myauto.targetClick(mySetting.PICTURE_RIGHTCHARA,5)
            myauto.abilityClick(4)
            time.sleep(rdInt)

            # 攻撃ボタンクリック
            myauto.click(410,490,40)
            # マウスカーソル退避
            pyauto.move(-300 + rdInt/5 , -100 - rdInt/5)
            # 攻撃し始めるまでのWait
            myauto.waitNotClickable(mySetting.PICTURE_ATTACK_CANCEL, 0.8)

        if wave < waveCount-1:
            # 攻撃し始めるまでのWait
            myauto.waitClickable(mySetting.PICTURE_PLAYERTURN)
            time.sleep(0.5)
            time.sleep(rdInt)
            reload()
    
        # PICTURE_OK 
        # myauto.waitBattleFinish()
        reload()   


myauto.click(1550,230,30)
print('実行終了')