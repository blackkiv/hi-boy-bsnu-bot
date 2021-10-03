from aiogram.types.message import ParseMode
from properties import BOT_TOKEN, DEFAULT_MESSAGE
import logging
from aiogram import Bot, Dispatcher, executor, types
from message_repository import MessageRepository
from msg_utils import create_message

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
repository = MessageRepository()


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.reply("я кароч слежу за тем, кто зашел..")


@dp.message_handler(commands=["set_message"])
async def set_message(message: types.Message):
    chat_id = message.chat.id

    sender = await bot.get_chat_member(chat_id, message.from_user.id)

    is_admin = sender.is_chat_admin() or sender.is_chat_creator()
    if not is_admin:
        await message.reply("only admin users can do this")
        return

    args = message.get_args()

    if not args or args.find("{MENTION}") == -1:
        await message.reply("invalid command argument")
        return

    await repository.save(chat_id, args)

    logging.log(logging.INFO, msg=f"welcome message changed in chat: {chat_id}")
    await message.reply("saved")


@dp.message_handler(commands=["show_message"])
async def show_message(message: types.Message):
    chat_id = message.chat.id

    try:
        welcome_message = await repository.get(chat_id)
    except:
        welcome_message = DEFAULT_MESSAGE

    logging.log(logging.INFO, msg=f"message showed for chat: {chat_id}")
    await message.reply(welcome_message)


@dp.message_handler(commands=["delete_message"])
async def delete_message(message: types.Message):
    chat_id = message.chat.id

    sender = await bot.get_chat_member(chat_id, message.from_user.id)

    is_admin = sender.is_chat_admin() or sender.is_chat_creator()
    if not is_admin:
        await message.reply("only admin users can do this")
        return

    await repository.delete(chat_id)

    logging.log(logging.INFO, msg=f"message deleted for chat: {chat_id}")
    await message.reply("message deleted")


@dp.message_handler(content_types=["new_chat_members"])
async def chat_member(message: types.Message):
    chat_id = message.chat.id
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
        member_mention = new_member.mention

    try:
        welcome_message = await repository.get(chat_id)
    except:
        welcome_message = DEFAULT_MESSAGE

    welcome_message = await create_message(member_mention, welcome_message)

    logging.log(logging.INFO, msg=f"new chat user: {new_member_username}")
    await bot.send_message(chat_id, welcome_message, parse_mode=ParseMode.HTML)


if __name__ == "__main__":
    print("start bot polling..")
    executor.start_polling(dispatcher=dp, skip_updates=True)
