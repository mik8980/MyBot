from telegram.ext import Updater, CommandHandler
def greet_user(update, context):
    print('Вызван /start :)')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start ')

def main():

    mybot = Updater("5151686095:AAEOQ9HpV40J2RwZ0Vfs_mnRachGLNE2n2Q", use_context = True)
   
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
   
    mybot.start_polling()
    mybot.idle()

main()