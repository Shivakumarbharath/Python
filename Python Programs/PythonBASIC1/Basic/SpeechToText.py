import speech_recognition as sr

# to recognise our audio
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything :")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said {}".format(text))

    except:
        print("could not recognise")
