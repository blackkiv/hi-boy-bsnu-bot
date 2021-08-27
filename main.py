from properties import BOT_TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.reply("я кароч слежу за тем, кто зашел..")


@dp.message_handler(content_types=["new_chat_members"])
async def chat_member(message: types.Message):
    new_member_username = message.new_chat_members[0].username
    if message.new_chat_members[0].is_bot:
        logging.log(logging.INFO, msg=f"bot added to group")
        return

    chat_id = message.chat.id
    text = f"👀✨ привет, @{new_member_username}..\nкакой курс, специальность, группа?\nизучал(а) программирование или онли школьные знания? (относится к первашам)"
    logging.log(logging.INFO, msg=f"new chat user: {new_member_username}")
    await bot.send_message(chat_id, text)


if __name__ == "__main__":
    print("start bot polling..")
    executor.start_polling(dispatcher=dp, skip_updates=True)
