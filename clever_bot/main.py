from cleverbotfree import Cleverbot
from googletrans import Translator
from gtts import gTTS
from random import randint
from playsound import playsound
import os

translator = Translator()

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
        if user_input == "q":
            break
        reply = bot.single_exchange(user_input_en)
        reply_tr = translate(bot_prompt, reply, "tr")
        speak(reply_tr)
        print(bot_prompt, reply_tr)
    bot.close()


chat("User : ", "Bot : ")
