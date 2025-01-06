from asyncio import run
from os import remove

from environs import Env
from telegram import Bot

from constants import COMICS_PATH
from downoload_tools import download_image
from requests_tools import fetch_random_comic
from telegram_tools import send_image


async def main():
    env = Env()
    env.read_env()

    token = env.str('TELEGRAM_TOKEN')
    chat_id = env.str('TELEGRAM_CHAT_ID')
    bot = Bot(token)

    comics_response = fetch_random_comic()
    image = comics_response.get('img')
    comment = comics_response.get('alt')
    if image:
        download_image(image, COMICS_PATH)
        await send_image(bot, chat_id, COMICS_PATH)
        remove(COMICS_PATH)
    if comment:
        await bot.send_message(chat_id=chat_id, text=comment)


if __name__ == '__main__':
    run(main())
