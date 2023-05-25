from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import webbrowser
import datetime
import tkinter as tk
from tkinter import *
import time
import winsound
from threading import *
import requests

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


def clock():
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


def stopwatch():
    global recognizer

    speaker.say("Opening Stopwatch App")

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                stopwatch = recognizer.recognize_google(audio)
                stopwatch.lower()

                speaker.say("The App has been opened, all you have to do is press the start button. To talk to me, "
                            "close the stopwatch app.")
                speaker.runAndWait()

                # Start of Stopwatch App code

                class StopWatch:
                    def __init__(self, master):
                        self.master = master
                        self.master.title("Stopwatch")

                        self.running = False
                        self.elapsed_time = 0
                        self.last_time = 0

                        self.time_label = tk.Label(self.master, text="00:00:00", font=("Arial", 30))
                        self.time_label.pack(pady=10)

                        self.start_button = tk.Button(self.master, text="Start", command=self.start_stopwatch)
                        self.start_button.pack(pady=5)

                        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_stopwatch)
                        self.reset_button.pack(pady=5)

                    def start_stopwatch(self):
                        self.running = not self.running
                        if self.running:
                            self.start_button.config(text="Stop")
                            self.update_time()
                        else:
                            self.start_button.config(text="Start")
                            self.master.after_cancel(self.job)

                    def update_time(self):
                        if self.running:
                            self.elapsed_time += time.time() - self.last_time
                            minutes, seconds = divmod(int(self.elapsed_time), 60)
                            hours, minutes = divmod(minutes, 60)
                            self.time_label.config(text="{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
                            self.last_time = time.time()
                            self.job = self.master.after(10, self.update_time)

                    def reset_stopwatch(self):
                        self.running = False
                        self.elapsed_time = 0
                        self.start_button.config(text="Start")
                        self.time_label.config(text="00:00:00")

                root = tk.Tk()
                stopwatch = StopWatch(root)
                root.mainloop()

                # End of Stopwatch App code

                done = True

                speaker.say("Hello what can I do for you?")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def quit():
    speaker.say('Goodbye, see you very soon!')
    speaker.runAndWait()
    sys.exit(0)


def timer():
    global recognizer

    speaker.say("Opening Timer App")

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                timer = recognizer.recognize_google(audio)
                timer.lower()

                speaker.say("The app has opened. Setting the timer will make you set it in seconds. "
                            "Just press the start button after that, and it will start. After it has ended, "
                            "it will beep for a little bit letting you know that it is over. If you want to talk to me,"
                            "just close the app.")
                speaker.runAndWait()

                # Start of Timer App

                class TimerApp:
                    def __init__(self, master):
                        self.master = master
                        self.seconds = tk.IntVar(value=60)
                        self.is_running = False

                        self.label = tk.Label(self.master,
                                              text=f"{self.seconds.get() // 60:02d}:{self.seconds.get() % 60:02d}",
                                              font=("Arial", 30))
                        self.label.pack()

                        self.spin_box = tk.Spinbox(self.master, from_=0, to=3600, increment=60,
                                                   textvariable=self.seconds,
                                                   font=("Arial", 20))
                        self.spin_box.pack()

                        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
                        self.start_button.pack(side=tk.LEFT, padx=10)

                        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer,
                                                     state=tk.DISABLED)
                        self.stop_button.pack(side=tk.RIGHT, padx=10)

                    def start_timer(self):
                        self.is_running = True
                        self.start_button.config(state=tk.DISABLED)
                        self.stop_button.config(state=tk.NORMAL)

                        while self.seconds.get() > 0 and self.is_running:
                            minutes, seconds = divmod(self.seconds.get(), 60)
                            time_str = f"{minutes:02d}:{seconds:02d}"
                            self.label.config(text=time_str)

                            self.master.update()
                            time.sleep(1)
                            self.seconds.set(self.seconds.get() - 1)

                        self.stop_timer()
                        self.play_sound()

                    def stop_timer(self):
                        self.is_running = False
                        self.start_button.config(state=tk.NORMAL)
                        self.stop_button.config(state=tk.DISABLED)

                    def play_sound(self):
                        frequency = 1000
                        duration = 1000
                        winsound.Beep(frequency, duration)

                root = tk.Tk()
                app = TimerApp(root)
                root.mainloop()

                # End of Timer App

                done = True

                speaker.say("Hello, what can I do for you?")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def alarm():
    global recognizer

    speaker.say("Opening Alarm App")

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                alarm = recognizer.recognize_google(audio)
                alarm.lower()

                speaker.say("The app has opened.It will have boxes where you can put the time you want to wake "
                            "up in. Just press the Set Alarm button to start your alarm. Info will be displayed in "
                            "the text box below for time. To talk to me, just close the app.")
                speaker.runAndWait()

                # Start of Alarm App

                root = Tk()
                root.geometry("400x200")

                def Threading():
                    t1 = Thread(target=alarm2)
                    t1.start()

                def alarm2():
                    while True:

                        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

                        time.sleep(1)

                        current_time = datetime.datetime.now().strftime("%H:%M:%S")
                        print(current_time, set_alarm_time)

                        if current_time == set_alarm_time:
                            print("Time to Wake up")
                            # Playing sound
                            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

                Label(root, text="Alarm Clock", font="Helvetica 20 bold", fg="red").pack(pady=10)
                Label(root, text="Set Time", font="Helvetica 15 bold").pack()

                frame = Frame(root)
                frame.pack()

                hour = StringVar(root)
                hours = ('00', '01', '02', '03', '04', '05', '06', '07',
                         '08', '09', '10', '11', '12', '13', '14', '15',
                         '16', '17', '18', '19', '20', '21', '22', '23', '24'
                         )
                hour.set(hours[0])

                hrs = OptionMenu(frame, hour, *hours)
                hrs.pack(side=LEFT)

                minute = StringVar(root)
                minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
                           '08', '09', '10', '11', '12', '13', '14', '15',
                           '16', '17', '18', '19', '20', '21', '22', '23',
                           '24', '25', '26', '27', '28', '29', '30', '31',
                           '32', '33', '34', '35', '36', '37', '38', '39',
                           '40', '41', '42', '43', '44', '45', '46', '47',
                           '48', '49', '50', '51', '52', '53', '54', '55',
                           '56', '57', '58', '59', '60')
                minute.set(minutes[0])

                mins = OptionMenu(frame, minute, *minutes)
                mins.pack(side=LEFT)

                second = StringVar(root)
                seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
                           '08', '09', '10', '11', '12', '13', '14', '15',
                           '16', '17', '18', '19', '20', '21', '22', '23',
                           '24', '25', '26', '27', '28', '29', '30', '31',
                           '32', '33', '34', '35', '36', '37', '38', '39',
                           '40', '41', '42', '43', '44', '45', '46', '47',
                           '48', '49', '50', '51', '52', '53', '54', '55',
                           '56', '57', '58', '59', '60')
                second.set(seconds[0])

                secs = OptionMenu(frame, second, *seconds)
                secs.pack(side=LEFT)

                Button(root, text="Set Alarm", font="Helvetica 15", command=Threading).pack(pady=20)

                root.mainloop()

                # End of Alarm App

                done = True

                speaker.say("Hello, what can I do for you?")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


def weather1():
    global recognizer

    speaker.say("Opening Weather App")

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                weather2 = recognizer.recognize_google(audio)
                weather2.lower()

                speaker.say("The app has just opened. It will have a text box where you"
                            "can type the city name to get the weather. If you want to "
                            "talk to me, just close the app.")
                speaker.runAndWait()

                # Start of Weather App

                def getweather(canvas):
                    city = textField.get()
                    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid" \
                                                                                        "=15b94c57aa5ae2b8bcb8fb"
                    "22cd1c9d9c"

                    json_data = requests.get(api).json()
                    condition = json_data['weather'][0]['main']
                    temp = int(json_data['main']['temp'] * 1.8 - 459.67)
                    min_temp = int(json_data['main']['temp_min'] * 1.8 - 459.67)
                    max_temp = int(json_data['main']['temp_max'] * 1.8 - 459.67)
                    pressure = json_data['main']['pressure']
                    humidity = json_data['main']['humidity']
                    wind = json_data['wind']['speed']
                    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
                    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

                    final_info = condition + "\n" + str(temp) + "°F"
                    final_data = "\n" + "Min Temp: " + str(min_temp) + "°F" + "\n" + "Max Temp: " + str(
                        max_temp) + "°F" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
                        humidity) + "\n" + "Wind Speed: " + str(
                        wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
                    label1.config(text=final_info)
                    label2.config(text=final_data)

                canvas = tk.Tk()
                canvas.geometry("600x500")
                canvas.title("Weather App")
                f = ("poppins", 15, "bold")
                t = ("poppins", 35, "bold")

                textField = tk.Entry(canvas, justify='center', width=20, font=t)
                textField.pack(pady=20)
                textField.focus()
                textField.bind('<Return>', getweather)

                label1 = tk.Label(canvas, font=t)
                label1.pack()
                label2 = tk.Label(canvas, font=f)
                label2.pack()
                canvas.mainloop()

                # End of Weather App

                done = True

                speaker.say("Hello, what can I do for you?")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "google_search": google_search,
    "youtube_music_tv": youtube_music_tv,
    "exit": quit,
    "clock": clock,
    "date": date,
    "stopwatch": stopwatch,
    "timer": timer,
    "alarm": alarm,
    "weather1": weather1
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
