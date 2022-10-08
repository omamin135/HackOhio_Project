import speech_recognition as sr
import pyttsx3
import time

class sttc:

    def stt():
        # Initialize the recognizer
        r = sr.Recognizer()

        # Function to convert text to
        # speech
            
            
        # Loop infinitely for user to
        # speak

        t_end = time.time() + 3

        while(time.time() < t_end):
            
            # Exception handling to handle
            # exceptions at the runtime
            try:
                
                # use the microphone as source for input.
                with sr.Microphone() as source2:
                    
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    
                    #listens for the user's input
                    audio2 = r.record(source2, duration = 3)
                    

                
                    
                    # Using google to recognize audio
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()

                    print("Did you say "+MyText)
                    
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
            except sr.UnknownValueError:
                print("unknown error occured")
        return MyText




