from os import path, remove

from environs import Env
from telegram import Bot

from constants import COMICS_PATH
from downoload_tools import download_image
from requests_tools import fetch_random_comic
from telegram_tools import send_image


def main():
    env = Env()
    env.read_env()

    token = env.str('TELEGRAM_TOKEN')
    chat_id = env.str('TELEGRAM_CHAT_ID')
    bot = Bot(token)

    try:
        random_comic = fetch_random_comic().json()
        image = random_comic.get('img')
        comment = random_comic.get('alt')
        if image:
            download_image(image, COMICS_PATH)
            send_image(bot, chat_id, COMICS_PATH)
        if comment:
            bot.send_message(chat_id=chat_id, text=comment)
    finally:
        if path.exists(COMICS_PATH):
            remove(COMICS_PATH)
            print(f'Temp file {COMICS_PATH} removed')


if __name__ == '__main__':
    main()
