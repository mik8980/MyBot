def wordcount(update, context):
    user_text = update.message.text.split()
    if len(user_text) == 1:
        update.message.reply_text('Я не считаю пустую строку')
        return
    words = user_text[1:]
    print(len(words))
    update.message.reply_text(len(words))