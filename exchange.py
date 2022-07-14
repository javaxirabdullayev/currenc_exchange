from telegram import ReplyKeyboardMarkup, ReplyMarkup, Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import requests

API_KEY = '8707e7c9b615971087c42f83'

url1 = f'https://v6.exchangerate-api.com/v6/8707e7c9b615971087c42f83/pair/USD/UZS'
url2 = f'https://v6.exchangerate-api.com/v6/8707e7c9b615971087c42f83/pair/EUR/UZS'
url3 = f'https://v6.exchangerate-api.com/v6/8707e7c9b615971087c42f83/pair/RUB/UZS'
url4 = f'https://v6.exchangerate-api.com/v6/8707e7c9b615971087c42f83/pair/GBP/UZS'

response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)

kurs1 = response1.json()['conversion_rate']
kurs2 = response2.json()['conversion_rate']
kurs3 = response3.json()['conversion_rate']
kurs4 = response4.json()['conversion_rate']

dollar = f"1 AQSH dollarining bugungi kunda so'mga nisbatan qiymati {kurs1} so'mga teng"
euro = f"1 Yevropa yevrosining bugungi kunda so'mga nisbatan qiymati {kurs2} so'mga teng"
rubl = f"1 Rossiya rublining bugungi kunda so'mga nisbatan qiymati {kurs3} so'mga teng"
pound = f"1 Angliya funt sterlingining bugungi kunda so'mga nisbatan qiymati {kurs4} so'mga teng"



def keyboard():
    buttons = [["Dollar", "Yevro"], ["Rubl", "Funt sterling"]]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)




def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user

    update.message.reply_html(
        f"Assalom alaykum, {user.mention_html()}! Siz bu bot orqali chet el valyutalarining so'mga nisbatan qiymatini bilib olishingiz mumkun", reply_markup=keyboard()
    )




def echo(update: Update, context: CallbackContext) -> None:
    if update.message.text=="Dollar":
        update.message.reply_text(f"{dollar}")
    elif update.message.text=="Yevro":
        update.message.reply_text(f"{euro}")
    elif update.message.text=="Rubl":
        update.message.reply_text(f"{rubl}")
    elif update.message.text=="Funt sterling":
        update.message.reply_text(f"{pound}")

     
def main() -> None:

    updater = Updater("5285906650:AAE-6cZpQEvf-JnkEtMj1s8Rl4DRER4cK7A")
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()



if __name__ == "__main__":

    main()