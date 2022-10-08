
import Get_Speech as gs
import json

#speechText = gs.myText
speechText = "mouse left click"


file = open(r"/Users/darreljobin/Documents/HackOHI:O Project Repo/HackOHI:O FrFr /HackOhio_Project/something.json")
cmd = json.load(file)
file.close()

array = speechText.split()
if array[0] == "type":

    cmd["commands"] = array[0]
    cmd["type"]["word"] = []
    for i in array[1]:
        cmd["type"]["word"].append(i)

elif array[0] == "mouse":

    cmd["commands"] = array[0]
    cmd["mouse"]["click"] = ""
    if array[-1] == "click":
        cmd["mouse"]["click"] = array[1]
    else:
        cmd["mouse"]["direction"] = array[1]
        cmd["mouse"]["distance"] = int(array[2])
    

file = open(r"/Users/darreljobin/Documents/HackOHI:O Project Repo/HackOHI:O FrFr /HackOhio_Project/something.json", "w")  
file.write(json.dumps(cmd))
file.close




