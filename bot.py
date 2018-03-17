from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
  update.message.reply_text("just tell me your mood or anything that you want from me..")
def convert_uppercase(bot, update):
  update.message.reply_text(update.message.text.upper())
def music(bot, update):
  update.message.reply_text("here are some songs you might like")
def video(bot, update):
  update.message.reply_text("here are the videos")
def article(bot, update):
  update.message.reply_text("these are some useful articles")
def movies(bot, update):
  update.message.reply_text("this is my fav movie list")
def sex(bot, update):
  update.message.reply_text("lets talk about sex")
def lifestyle(bot, update):
  update.message.reply_text("ways to improve our lifestyle")
def humour(bot, update):
  update.message.reply_text("knock knock!")
def depressed(bot, update):
  update.message.reply_text("aur batao bosdike")
def bored(bot, update):
  update.message.reply_text("whtsup bitchessss!!")
def philosophy(bot, update):
  update.message.reply_text("aur batao bosdike")
def random(bot, update):
  update.message.reply_text("whtsup bitchessss!!")
def aurbatao(bot, update):
  update.message.reply_text("aur batao bosdike")


def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater("522134488:AAEciBRp0-stiUy8upRD9meB1HRzNOKtyAw")
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(upper_case)

  start_handler2 = CommandHandler('music',music)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler2)
  dispatcher.add_handler(upper_case)

  start_handler3 = CommandHandler('video',video)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler3)
  dispatcher.add_handler(upper_case)

  start_handler4 = CommandHandler('article',article)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler4)
  dispatcher.add_handler(upper_case)

  start_handler5= CommandHandler('movies',movies)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler5)
  dispatcher.add_handler(upper_case)

  start_handler6 = CommandHandler('sex',sex)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler6)
  dispatcher.add_handler(upper_case)

  start_handler7= CommandHandler('lifestyle',lifestyle)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler7)
  dispatcher.add_handler(upper_case)

  start_handler8 = CommandHandler('humour',humour)
  upper_case = MessageHandler(Filters.text, convert_uppercase)

  dispatcher.add_handler(start_handler8)
  dispatcher.add_handler(upper_case)


  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()
