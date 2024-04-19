from cleverbotfree import Cleverbot
from googletrans import Translator
from gtts import gTTS
from random import randint
from playsound import playsound
import os
import speech_recognition as sr


translator = Translator()
rec = sr.Recognizer()

def record():
    with sr.Microphone() as source:
        voice_rec = ""
        audio = rec.listen(source, 5, 5)
        try:
            voice_rec = rec.recognize_amazon(audio)
        except:
            speak("Anlamadım")

    return voice_rec


def speak(text):
    tts = gTTS(text)
    rand = randint(1, 100000)
    file = "audio." + str(rand) + ".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def translate(who, text, lang):
    translated = translator.translate(text, dest=lang)
    return translated.text

@Cleverbot.connect
def chat(bot, user_prompt, bot_prompt):
    while True:
        user_input = input(user_prompt)
        user_input_en = translate(user_prompt, user_input, "en")
        #print(user_prompt, user_input_en)
        if user_input == "q":
            break
        reply = bot.single_exchange(user_input_en)
        #print(bot_prompt, reply)
        reply_tr = translate(bot_prompt, reply, "tr")
        #speak(reply_tr)
        print(bot_prompt, reply_tr)
    bot.close()


chat("User : ", "Bot : ")
