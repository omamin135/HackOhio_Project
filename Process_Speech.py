import Get_Speech as gs
import json


class Ps:

    def process(speechText):
        
        print(speechText)
        # speechText = "mouse left click"


        cmd = {"commands": "", "mouse": {"direction": "", "distance": 0, "click": ""}, "input": {"word": []}}
        
        array = speechText.split()
        print(array)
        if array[0] == "input":

            cmd["commands"] = array[0]
            cmd["input"]["word"] = []
            for i in range(1, len(array)):
                if (i != 1):
                    cmd["input"]["word"].append(" ")
                for char in array[i]:
                    cmd["input"]["word"].append(char)

        elif array[0] == "mouse":

            cmd["commands"] = array[0]
            cmd["mouse"]["click"] = ""
            if array[-1] == "click":
                cmd["mouse"]["click"] = array[1]
            else:
                cmd["mouse"]["direction"] = array[1]
                cmd["mouse"]["distance"] = int(array[2])
            
        return cmd
     






