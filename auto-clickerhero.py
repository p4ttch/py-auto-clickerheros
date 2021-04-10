# library comes from : https://pyautogui.readthedocs.io/en/latest/quickstart.html
import pyautogui as pg
import time
import threading

#Objective:
# Make a Clicker Heros bot to progress in levels
# Click the monsters 10 times 
# then try move to next level + click for upgrades
# then reset the clicker counter and repeat
# Note: this script is designed for a laptop with screen Size(width=1366, height=768)

# config
loopPhaseClicks=50

# variables
clicks = 0
gamePhase = 0

# gamePhase 0
def killmonsters(clickCounter):
    clicks = clickCounter
    global gamePhase
    global loopPhaseClicks
    #Move mouse to hover over monsters
    pg.moveTo(999, 429, duration=0.1)
    print("Smash the monsters: "+str(gamePhase))
    while clicks < loopPhaseClicks :
        pg.click()
        pg.click()
        clicks += 1
        print("clicks:"+ str(clicks), end = "\r")
    gamePhase +=1
    print("")

# gamePhase 1
def nextlevel():
    global gamePhase
    #click on next level
    pg.moveTo(1060, 73, duration=0.1)
    pg.click()
    gamePhase +=1
    print("Move 1 level up: "+str(gamePhase))

def grindMoreGold():
    global gamePhase
    #click on next level
    pg.moveTo(848, 73, duration=0.1)
    pg.click()
    gamePhase +=1
    print("Move 2 levels back, Grind more gold: "+str(gamePhase))

def damageBoost():
    #clickstorm
    pg.moveTo(730, 222, duration=0.1)
    pg.click()
    # Powersurge
    pg.moveTo(730, 260, duration=0.1)
    pg.click()
    # lucky Strikes
    pg.moveTo(730, 330, duration=0.1)
    pg.click()
    # Metal Detector
    pg.moveTo(730, 380, duration=0.1)
    pg.click()
    print("Run Powerups for boss")

# gamePhase 2
def upgrade():
    global gamePhase
    #click for upgrades
    pg.moveTo(157, 274, duration=0.1)
    pg.click()
    pg.click()
    pg.moveTo(157, 377, duration=0.1)
    pg.click()
    pg.click()
    pg.moveTo(157, 477, duration=0.1)
    pg.click()
    pg.click()
    gamePhase +=1
    print("Upgrade Damage: "+str(gamePhase))

# gamePhase 2
def resetLoop():
    global gamePhase
    global clicks
    clicks = 0
    gamePhase = 0
    print("loop is resetting, waiting 5 seconds")
    for count in range(5):
        print(time.ctime(), end = "\r")
        # Prints the current time with a five second difference
        time.sleep(1) # important pause to regain control of the mouse haha.


def phase_manager():        
    while gamePhase < 12:
        #kill monsters to grind gold and attempt next level 4 times
        # 1
        if (gamePhase == 0):
            killmonsters(clicks)
        if (gamePhase == 1):
            nextlevel()
        # 2
        if (gamePhase == 2):
            killmonsters(clicks)
        if (gamePhase == 3):
            nextlevel()
        # 3
        #back to boss, Boss boost damage goes here
        if (gamePhase == 4):
            damageBoost()
            killmonsters(clicks)
        if (gamePhase == 5):
            nextlevel()
        # 3
        if (gamePhase == 6):
            killmonsters(clicks)
        if (gamePhase == 7):
            nextlevel()
        # go back
        if (gamePhase == 8):
            killmonsters(clicks)
        if (gamePhase == 9):
            grindMoreGold()

        #upgrades + reset
        if (gamePhase == 10):
            upgrade()
        if (gamePhase == 11):
           resetLoop()

print("The script will start in 5 seconds. Please get your clicker hero window ready.")
for count in range(5):
        print(time.ctime(), end = "\r")
        time.sleep(1)

phase_manager()

# I dont think threading would work well for the normal auto clicker as far as going up in levels just yet, but maybe if i shuffled some things around. But it does increase the speed of clicks greatly hahaha
# threads = []

# for i in range(5):
#     t = threading.Thread(target=phase_manager)
#     t.daemon = True
#     threads.append(t)

# for i in range(5):
#     threads[i].start()

# for i in range(5):
#     threads[i].join()
    