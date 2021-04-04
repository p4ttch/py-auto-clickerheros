# library comes from : https://pyautogui.readthedocs.io/en/latest/quickstart.html
import pyautogui as pg
import time

#Objective:
# Make a Clicker Heros bot to progress in levels
# Click the monsters 10 times 
# then try move to next level + click for upgrades
# then reset the clicker counter and repeat
# Note: this script is designed for a laptop with screen Size(width=1366, height=768)

clicks = 0
gamePhase = 0

# gamePhase 0
def killmonsters(clickCounter):
    clicks = clickCounter
    global gamePhase
    #Move mouse to hover over monsters
    pg.moveTo(999, 429, duration=0.1)
    while clicks < 20 :
        pg.click()
        pg.click()
        clicks += 1
        print("clicks:"+ str(clicks))
    gamePhase +=1
    print(gamePhase)

# gamePhase 1
def nextlevel():
    global gamePhase
    #click on next level
    pg.moveTo(1060, 73, duration=0.1)
    pg.click()
    gamePhase +=1
    print(gamePhase)

# gamePhase 2
def upgrade():
    global gamePhase
    #click for upgrades
    pg.moveTo(157, 274, duration=0.1)
    pg.click()
    gamePhase +=1
    print(gamePhase)

# gamePhase 2
def resetLoop():
    global gamePhase
    global clicks
    clicks = 0
    gamePhase = 0
    print("loop is resetting, waiting 5 seconds")
    for count in range(5):
        print(time.ctime())
        # Prints the current time with a five second difference
        time.sleep(1) # important pause to regain control of the mouse haha.

print("The script will start in 5 seconds. Please get your clicker hero window ready.")
for count in range(5):
        print(time.ctime())
        time.sleep(1)
while gamePhase < 4:
    if (gamePhase == 0):
        killmonsters(clicks)
    if (gamePhase == 1):
        nextlevel()
    if (gamePhase == 2):
        upgrade()
    if (gamePhase == 3):
       resetLoop()
# killmonsters(clicks)
    