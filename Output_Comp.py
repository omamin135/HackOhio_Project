import pyautogui as pg
import json

import Get_Speech as gs


PIXEL_DENSITY = 165.63 #inches


def getCmd():
    f = open(r"C:\Users\omami\Desktop\Code\Speech_Project\HackOhio_Project\something.json")
    cmd = json.load(f)
    f.close()
    return cmd


class ProcessEvents():

    def __init__(self, cmd):
        self.cmd = cmd
        
    def mmToPixels(self, dist):
        return PIXEL_DENSITY / 24.4 * dist
    
    def moveMouse(self, distance, direction):

        inches = distance
        pix = self.mmToPixels(inches)

        if direction == "left":
            pg.move(-pix, 0)
        elif direction == "right":
            pg.move(pix, 0)
        elif direction == "up":
            pg.move(0, -pix)
        elif direction == "down":
            pg.move(0, pix)

    def clickMouse(self, butt):
        pg.click(button=butt)


    # def ctrlProcess(self, key):
    #     with pg.hold("ctrl"):
    #         pg.press(key)

    def keyPress(self, word):
        pg.press(word)



class OC: 
    def process(commands):
    # commands = getCmd()

        do = ProcessEvents(commands)

        cmdType = commands["commands"]

        if (cmdType == "mouse"):
            click = commands["mouse"]["click"]
            if (click == "left" or click == "right"):
                do.clickMouse(click)
            else:
                distance = commands["mouse"]["distance"]
                direction = commands["mouse"]["direction"]
                do.moveMouse(distance, direction)
                
        elif (cmdType == "input"):
            word = commands["input"]["word"]
            do.keyPress(word)




