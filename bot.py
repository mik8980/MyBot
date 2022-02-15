from telegram.ext import Updater

def main():

    mybot = Updater("5151686095:AAEOQ9HpV40J2RwZ0Vfs_mnRachGLNE2n2Q", use_context = True)
    mybot.start_polling()
    mybot.idle()

main()