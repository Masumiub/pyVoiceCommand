import speech_recognition as sr
import pyttsx3


def listen_and_respond():
    r = sr.Recognizer()
    tts = pyttsx3.init()

    #listen for user input
    with sr.Microphone() as source:
        print("Listening. Please Tell Something....")
        audio = r.listen(source)

    # convert the audio to text and respond to the user's input
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

        # respond to the user's input
        if "hello" in text:
            tts.say("Hello! How can I help you?")
        elif "what time is it" in text:
            tts.say("It is currently X o'clock")
        else:
            tts.say("I'm sorry, I didn't understand what you said")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said")
        tts.say("I'm sorry, I didn't understand what you said")
    except sr.RequestError as e:
        print("Error occurred : {0}".format(e))

while True:
    listen_and_respond()


