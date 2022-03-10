import datetime
import ephem

def next_full_moon(update, context):
    today =  datetime.datetime.today()
    next_moon = ephem.next_full_moon(today)
    update.message.reply_text(f'Next full moon {next_moon}')