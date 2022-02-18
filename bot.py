import logging
import ephem
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings 

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print('Вызван /start ')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start ')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_planet(update, context):
    user_text = update.message.text.split()
    if len(user_text) == 1: 
        update.message.reply_text('Введите планету')
        return
    planet = user_text[1]
    answer = ''
    if bool(planet):
        if planet == 'Mars':
            answer = ephem.constellation(ephem.Mars('19/02/2022'))
        elif planet == 'Jupiter':
            answer = ephem.constellation(ephem.Jupiter('19/02/2022'))
        else: 
            answer = 'Нет информации'  
    update.message.reply_text(answer)



def main():


    mybot = Updater(settings.API_KEY, use_context = True)
   
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet ))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
  
  
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()