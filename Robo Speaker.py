import pyttsx3
engine = pyttsx3.init()
print("Welcome to my Text to Voice converter Program...")
a = "Nice talk with you. Bye bye..."
while True:
    text = input("Type something to speak (type 'End' to exit): ")
    if text.lower() == 'end':
        engine.say(a)
        engine.runAndWait()
        print("Nice talk with you. Bye bye...")
        break
    engine.say(text)
    engine.runAndWait()
