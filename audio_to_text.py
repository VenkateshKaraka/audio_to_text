import speech_recognition as sr 
def main():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("plz say something")
        audio=r.listen(source)
        print("Recognizing now ....")
        # recognizing speech using google
        try:
            print("You said that\n" + r.recognize_google(audio))
            print("audio recorded successfuly\n")
        except Exception as e:
            print("Error : "+str(e))
            #write audio
        with open("recorded.wav","wb") as f:
            f.write(audio.get_wav_data())
if __name__ == "__main__":
    main()

        

