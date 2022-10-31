import telebot

from django_shop import settings


class MessageSender:
    def __init__(self, chat_id: int, token: str):
        self.chat_id = chat_id
        self.bot = telebot.TeleBot(token, parse_mode='HTML')

    def send(self, username: str, question: str) -> None:
        text = ('<b>Новый вопрос в поддержку</b>\n\n'
                f'<b>Пользователь:</b> @{username.replace("@", "")}\n'
                f'<b>Вопрос:</b> <code>{question}</code>')
        self.bot.send_message(self.chat_id, text)


bot = MessageSender(settings.telegram_chat_id, settings.telegram_token)