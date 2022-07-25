import time
from pynput.mouse import Button, Controller
mouse = Controller()

time.sleep(3)

def leftClick(xPos, yPos, bufferTime):
    mouse.position = (xPos, yPos)
    time.sleep(1)
    mouse.click(Button.left, 1) 
    time.sleep(bufferTime)

def doubleClick(xPos, yPos, bufferTime):
    mouse.position = (xPos, yPos)
    time.sleep(1)
    mouse.click(Button.left, 2)
    time.sleep(bufferTime)

while True:
    doubleClick(141, 361, 3) # open chrome tab
    doubleClick(868, 67, 3) # maximize chrome tab cuz of weird glitch
    leftClick(1817, 168, 3) # open google apps
    leftClick(1712, 502, 2) # click calendar app
    leftClick(646, 676, 4) # click calendar item
    leftClick(956, 604, 4) # click google meet link
    leftClick(717, 813, 2) # Turn off Camera
    leftClick(619, 814, 3) # Turn off mic
    leftClick(1351, 632, 3) # Ask to join meeting

    time.sleep(10)