from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import webbrowser
import datetime

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = []


def hello():
    speaker.say("Hello, what can I do for you?")
    speaker.runAndWait()


def create_note():
    global recognizer

    speaker.say("What do you want to write on your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you! Please try again!")
            speaker.runAndWait()


def add_todo():
    global recognizer

    speaker.say("What to do do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say(f"I added {item} to the to do list!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def show_todos():
    global recognizer

    speaker.say("The items on your to do list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def google_search():
    global recognizer

    speaker.say("What do you want to search up?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                search = recognizer.recognize_google(audio)
                search = search.lower()

                url = "https://www.google.com/search?q=" + search + "&source=hp&ei=6M4DZL2FM6esqtsPlv-jgAE&iflsig" \
                                                                    "=AK50M_UAAAAAZAPc-Cycv03AZWt9P9UsdO6ZgaPkXI-N" \
                                                                    "&ved=0ahUKEwi9mcHfscP9AhUnlmoFHZb_CBAQ4dUDCAo" \
                                                                    "&uact=5&oq=hello&gs_lcp" \
                                                                    "=Cgdnd3Mtd2l6EAMyCAguEIAEELEDMgQIABBDMg" \
                                                                    "QILhBDMgsILhDUAhCxAxCABDIOCC4QgAQQsQMQxwEQ0" \
                                                                    "QMyBAgAEEMyEQguEIAEELEDEIMBEMcBEK8BMggILhCABB" \
                                                                    "DUAjIFCAAQgAQyCAgAELEDEIMBOhAILhDHARDRAxDqAhC0" \
                                                                    "AhBDOgoIABDqAhC0AhBDOhcILhDUAhDqAhC0AhCKAxC3AxD" \
                                                                    "UAxDlAjoUCAAQ6gIQtAIQigMQtwMQ1AMQ5QI6FAguEOoCELQ" \
                                                                    "CEIoDELcDENQDEOUCOhEILhCABBCxAxCDARDHARDRAzoICAAQ" \
                                                                    "gAQQsQM6CgguEMcBENEDEEM6BwguELEDEEM6CwguEIAE" \
                                                                    "ELEDENQCOggILhCxAxCDAVDLCViGEmDrE2gBcAB4AIABo" \
                                                                    "AGIAfgDkgEDNC4xmAEAoAEBsAEK&sclient=gws-wiz"
                webbrowser.open(url)
                done = True

                speaker.say("I have just opened the new website in your browser!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def youtube_music_tv():
    global recognizer

    speaker.say("What do you want to watch or listen to?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                tv_music = recognizer.recognize_google(audio)
                tv_music.lower()

                url = "https://www.youtube.com/results?search_query=" + tv_music
                webbrowser.open(url)
                done = True

                speaker.say("I have just opened youtube.com in your browser, have a nice time!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def time():
    global recognizer

    speaker.say("The time is: ")

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                time = recognizer.recognize_google(audio)
                time.lower()

                now = datetime.datetime.now()
                formatted_time = now.strftime("%I:%M %p")
                done = True

                speaker.say(formatted_time)
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def date():
    global recognizer

    speaker.say("The date is: ")

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                date = recognizer.recognize_google(audio)
                date.lower()

                now = datetime.datetime.now()
                formatted_date = now.strftime("%A, %B %d, %Y")
                done = True

                speaker.say(formatted_date)
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def quit():
    speaker.say('Goodbye, see you very soon!')
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "google_search": google_search,
    "youtube_music_tv": youtube_music_tv,
    "exit": quit,
    "time": time,
    "date": date
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
