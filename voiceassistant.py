import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error connecting to Google API: {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")

    while True:
        query = listen()

        if "exit" in query:
            speak("Goodbye!")
            break
        elif "your_name" in query:
            speak("I am a voice assistant created using Python.")
        else:
            speak("Sorry, I don't understand that command. Can you please repeat?")
            