from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests
from random import randint
import re
from config import *

def goStart(bot, update):
	chat_id = update.message.chat_id
	bot.send_message(
		chat_id = chat_id,
		text = "Hello buddy"
		)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def sendDog(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def sendAnime(bot, update):
	randPicNum = str(randint(1, 100001))
	url = 'https://www.thiswaifudoesnotexist.net/example-' + randPicNum + '.jpg'
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url)


def main():
	bot = Bot(token=TG_TOKEN, base_url=TG_API_URL)
	updater = Updater(bot=bot)
	pic_anime_handler = CommandHandler("anime", sendAnime)
	pic_dog_handler = CommandHandler("dog", sendDog)
	start_handler = CommandHandler("start", goStart)
	message_handler = MessageHandler(Filters.text, goStart)
	updater.dispatcher.add_handler(pic_anime_handler)
	updater.dispatcher.add_handler(pic_dog_handler)
	updater.dispatcher.add_handler(start_handler)
	updater.dispatcher.add_handler(message_handler)
	updater.start_polling()
	updater.idle()
if __name__ == '__main__':
	main()