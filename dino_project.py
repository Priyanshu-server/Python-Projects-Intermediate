#pyautogui
#pillow
import pyautogui
from PIL import Image,ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def collision(data):
    #loop for cactus
    for i in range(365,425):
        for j in range(625,655):
            if data[i,j] <100:
                hit('up')
                return


    #loop for bird
    for i in range(260,300):
        for j in range(450,555):
            if data[i,j] <100:
                hit('down')
                time.sleep(0.2)
                pyautogui.keyDown('down') #releasing the key
                return


    return






time.sleep(2)
while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    # #for cactus
    # for i in range(365,425):
    #     for j in range(625,655):
    #         data[i,j] = 0
    # #for bird
    # for i in range(260,300):
    #     for j in range(450,555):
    #         data[i,j] = 150
    
    # image.show()
    # break
    collision(data)
