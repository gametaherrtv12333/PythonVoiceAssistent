import speech_recognition
import webbrowser
import os
import pyttsx3
from g4f.client import Client


engine = pyttsx3.init()
ru_zira = 'HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Speech/Voices/Tokens/TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', ru_zira)
engine.setProperty('rate', 170)     # скорость речи
engine.setProperty('volume', 1)   # громкость речи


def question(user_text):
    return user_text


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.6


with speech_recognition.Microphone() as mic:
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio, language="ru-RU", show_all=False).lower()


if query == "открой гугл" or query == "открой google":
    engine.say("Открываю гугл")
    engine.runAndWait()
    webbrowser.open("google.ru")
if query == "открой ютуб" or query == "открой youtube":
    engine.say("Открываю ютуб")
    engine.runAndWait()
    webbrowser.open("youtube.ru")
if query == "открой фоторедактор" or query == "open photoeditor" or query == "открой photopea" or query == "открой photoshop" or query == "открой фотошоп":
    engine.say("Открываю фоторедактор")
    engine.runAndWait()
    webbrowser.open("photopea.com")
if query == "открой дискорд" or query == "открой discord" or query == "open discord":
    engine.say("Открываю дискорд")
    engine.runAndWait()
    webbrowser.open("discord.com")
if query == "открой гдз" or query == "открой gdz":
    engine.say("Открываю гдз")
    engine.runAndWait()
    webbrowser.open("gdz.ru")
if query == "включи чат gpt" or query == "включи чат гпт" or query == "open chat gpt" or query == "чат gpt":
    engine.say("Скажите что вы хотите узнать от чат gpt")
    engine.runAndWait()
    with speech_recognition.Microphone() as mic:
        quest = sr.listen(source=mic)
        complete_quest = sr.recognize_google(quest, language="ru-RU", show_all=False).lower()


    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{question(complete_quest)}"}],
    )

    print(response.choices[0].message.content)
    txt = response.choices[0].message.content
    engine.say(txt)
    engine.runAndWait()

if query == "открой сайт о программировании" or query == "открой сайт метанит" or query == "открой сайт metanit" or query == "программирование":
    engine.say("Открываю метанит")
    engine.runAndWait()
    webbrowser.open("metanit.com")
if query == "найди в гугле" or query == "в гугле":
    engine.say("К вашим услугам сер скажите что вы хотите найти")
    engine.runAndWait()
    with speech_recognition.Microphone() as mic:
        search = sr.listen(source=mic)
        searching = sr.recognize_google(search, language="ru-RU", show_all=False).lower()
    webbrowser.open(f"google.ru/search?q={searching}")
if query == "открой кап кут" or query == "открой cap cut" or query == "открой capcut":
    os.startfile("E:\capCut\capcut.exe")






print(query)