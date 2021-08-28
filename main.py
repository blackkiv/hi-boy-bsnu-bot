from aiogram.types.message import ParseMode
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
    new_member = message.new_chat_members[0]
    if new_member.is_bot:
        logging.log(logging.INFO, msg=f"bot added to group")
        return

    new_member_username = new_member.username
    if new_member_username == None:
        new_member_fullname = new_member.full_name
        new_member_id = new_member.id
        member_mention = f'<a href="tg://user?id={new_member_id}">{new_member_fullname}</a>'
    else:
        member_mention = f'@{new_member_username}'

    chat_id = message.chat.id
    text = f"👀✨ привет, {member_mention}\nкакой курс, специальность, группа?\n(ДЛЯ ФКН) -> изучал(а) программирование или онли школьные знания? (относится к первашам)"
    logging.log(logging.INFO, msg=f"new chat user: {new_member_username}")
    await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML)


if __name__ == "__main__":
    print("start bot polling..")
    executor.start_polling(dispatcher=dp, skip_updates=True)
