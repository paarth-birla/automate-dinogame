import pyautogui
from PIL import ImageGrab # ImageGrab ==> screenshot
import  time

def hit(key):
    pyautogui.keyDown(key)


def grab_image():
    image = ImageGrab.grab().convert('L')
    return image

def collide(data):
    for i in range(300, 415):
        for j in range(410, 560):
            if data[i, j] < 100:
                hit('down')
                return 

    for i in range(300, 415):
        for j in range(560, 660):
            if data[i, j] < 100:
                hit('up')
                return 
    
    return 


if __name__ == "__main__" :
    time.sleep(3)
    while True:
        image = grab_image()
        data = image.load()
        if collide(data):
            hit("up")

