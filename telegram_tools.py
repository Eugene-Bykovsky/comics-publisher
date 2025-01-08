def send_image(bot, chat_id, image_path):
    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id=chat_id, photo=image)
