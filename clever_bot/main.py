from cleverbotfree import Cleverbot


@Cleverbot.connect
def chat(bot, user_prompt, bot_prompt):
    while True:
        user_input = input(user_prompt)
        if user_input == "q":
            break
        reply = bot.single_exchange(user_input)
        print(bot_prompt, reply)
    bot.close()


chat("User : ", "Bot : ")
