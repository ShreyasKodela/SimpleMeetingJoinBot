import time
from pynput.mouse import Button, Controller
mouse = Controller()

time.sleep(5) # wait until ready
print(mouse.position) # print current (x,y)