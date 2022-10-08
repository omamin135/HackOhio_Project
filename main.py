import Get_Speech
import Process_Speech
import Output_Comp
import keyboard as k

while (1):    
    myText = Get_Speech.sttc.stt()
    cmd = Process_Speech.Ps.process(myText)
    print(cmd)
    Output_Comp.OC.process(cmd)



