####################################
# A little script I made for quickly
# opening/closing the "Unhook" 
# web extension for YouTube.
# 
# Purpose: To save a couple seconds
# TODO(Gabe): Optimise GPU utilisation
####################################

from pyautogui import position, locateOnScreen, moveTo, click, move
from keyboard import is_pressed
from time import sleep

def LocateImageAndMove() -> None:
    # get current mouse pos
    originalMousePos = position()

    # testing to find first image (when its closed at first)
    try:
        # OPEN GUI
        # Find the image, move to it, and click it 
        logoLocation1 = locateOnScreen('logo1.png', confidence=0.9)
        moveTo(logoLocation1)
        click()
        sleep(0.1)
        # INTERACT WITH GUI
        turnOnLocation = locateOnScreen("turnOn.png", confidence=0.8)
        moveTo(turnOnLocation)

        click()
        # THEN EXIT GUI
        moveTo(logoLocation1)
        click()
        print("turned on")


    except Exception as e:
        print(e)
        # print("FAILED turning on")

    # testing to find second image (when its open already)
    try:
        # OPEN GUI
        # Find the image, move to it, and click it 
        logoLocation2 = locateOnScreen('logo2.png', confidence=0.9)
        moveTo(logoLocation2)
        # click()
        sleep(0.1)
        # INTERACT WITH GUI
        move(-20, 35)
        click()

        # EXIT THE GUI
        moveTo(logoLocation2)
        click()
        
        sleep(0.1)
        print("turned off")

    except Exception as e:
        print(e)
        # print("FAILED turning off")

    # then go back to original position
    moveTo(originalMousePos)



def main():
    # infinite loop to check 
    shouldExit = False
    while not shouldExit:
        # check for CTRL+Q
        if (is_pressed('ctrl+q')):
            LocateImageAndMove()
            sleep(0.1) # cooldown period
        sleep(0.01) #optimise gpu usage

    



if __name__ == "__main__":
    main()