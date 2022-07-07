# exchangerate-api.com

import logging
import requests

API_KEY = '8707e7c9b615971087c42f83'

API_TOKEN = '5381092837:AAEXaV8hgIE3O_Y0PnQLhgpKdaPu4n1IozQ'

currency1 = 'USD'
currency2 = 'UZS'

url = f'https://v6.exchangerate-api.com/v6/8707e7c9b615971087c42f83/pair/{currency1}/{currency2}'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("")




response = requests.get(url)
print(response.json())


kurs = response.json()['conversion_rate']

print(f"Bugungi o'zbek so'mining 1 AQSH dollarga nisbatan qiymati: {kurs} so'mga teng.")