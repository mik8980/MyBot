import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from commands.get_planet import get_planet
from commands.start import greet_user
from commands.talk_to_me import talk_to_me
from commands.wordcount import wordcount
from commands.next_full_moon import next_full_moon

import settings 

logging.basicConfig(filename='bot.log', level=logging.INFO)



def main():


    mybot = Updater(settings.API_KEY, use_context = True)
   
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet ))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
  
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()