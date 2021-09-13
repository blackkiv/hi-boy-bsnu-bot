import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
MONGODB_HOST = os.environ.get("MONGODB_HOST")
MONGODB_PORT = os.environ.get("MONGODB_PORT")
MONGODB_CONNECTION_STRING = f"mongodb://{MONGODB_HOST}:{MONGODB_PORT}"
DEFAULT_MESSAGE = "👀✨ привет, {MENTION}\nкакой курс, специальность, группа?\n(ДЛЯ ФКН) -> изучал(а) программирование или онли школьные знания? (относится к первашам)"
