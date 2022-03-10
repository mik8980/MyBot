import datetime  
import ephem

def get_planet(update, context):
    today = datetime.datetime.today()
    user_text = update.message.text.split()
    if len(user_text) == 1: 
        update.message.reply_text('Введите планету')
        return
    planet = user_text[1]
    answer = ''
    if bool(planet):
        if planet == 'Mars':
            answer = ephem.constellation(ephem.Mars(today))
        elif planet == 'Jupiter':
            answer = ephem.constellation(ephem.Jupiter(today))
        else: 
            answer = 'Нет информации'  
    print('work')
    update.message.reply_text(answer)