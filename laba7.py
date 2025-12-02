import os
from dotenv import load_dotenv
import telebot

# Завантажуємо змінні з .env файлу
# Вказуємо явно кодування UTF-8
load_dotenv(encoding='utf-8')

# Отримуємо токен з .env або змінної середовища
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TOKEN:
    raise ValueError("Токен не знайдено! Перевірте файл .env або створіть його з рядком: TELEGRAM_BOT_TOKEN=ваш_токен")

# Створюємо бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    """Функція, яка відповідає на повідомлення тим самим текстом"""
    try:
        # Відправляємо те саме повідомлення назад
        bot.reply_to(message, message.text)
    except Exception as e:
        print(f"Помилка при відправці повідомлення: {e}")


if __name__ == '__main__':
    print("Бот запущено! Натисніть Ctrl+C для зупинки.")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Помилка: {e}")

