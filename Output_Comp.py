import pyautogui as pg
import Get_Speech as gs



PIXEL_DENSITY = 165.63


def getCmd():
    pass


class ProcessMouseEvents():

    def __init__(self, cmd):
        
        self.cmd = cmd

    def inchToPixels(self, inches):
        return PIXEL_DENSITY * inches
    
    def convertToInch(self):
        #TODO: convert sting length into an integer
        pass

    def moveMouse(self):

        inches = self.convertToInch()
        pix = self.inchToPixels(inches)

        if self.cmd == "left":


        pg.move()


        


    





