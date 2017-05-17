import speech_recognition as sr
def recognize():
    r = sr.Recognizer()
    text = "ERROR"
    with sr.Microphone() as source:
        r.energy_threshold = 3000
        r.dynamic_energy_threshold = True
        #r.adjust_for_ambient_noise(source)
        print("Im listening adventurer...")
        audio = r.listen(source)
    try:
        text = r.recognize_sphinx(audio)
    except sr.UnknownValueError:
        text = "I don't understand..."
    except sr.RequestError as e:
        text = "ERROR"
    print(text)
    return text
