async def create_message(mention: str, message: str):
    return message.replace("{MENTION}", mention)
