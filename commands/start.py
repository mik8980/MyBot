def greet_user(update, context):
    print('Вызван /start ')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start ')