from telegram.client import Telegram

tg = Telegram(
    api_id=25332790,
    api_hash="417b3a602673ffc98602688051b71c58",
    phone="+6594510169",
    database_encryption_key="password"
)


def new_message_handler(update):
    print(update)


tg.login()
tg.add_message_handler(new_message_handler)
tg.idle()
