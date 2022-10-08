import Get_Speech
import keyboard as k

while (1):    
    try:
        if k.is_pressed('space'):
            print("ending")
            break
    except:
        while (True):
            Get_Speech.sttc.stt()


