from datetime import date
from motor import motor_asyncio
from properties import MONGODB_ATLAS_URL


class MessageRepository(object):
    def __init__(self):
        global mongo
        global spy
        client = motor_asyncio.AsyncIOMotorClient(MONGODB_ATLAS_URL)
        print(client.server_info())
        mongo = client["msg"]["messages"]
        spy = client["dima"]["messages"]

    async def save(self, chat_id: str, message: str):
        await self.delete(chat_id)
        document = {"chat_id": chat_id, "message": message}
        await mongo.insert_one(document)

    async def get(self, chat_id: str):
        result = await mongo.find_one({"chat_id": chat_id})
        return result["message"]

    async def delete(self, chat_id: int):
        await mongo.delete_many({"chat_id": chat_id})

    async def save_spy(self, chat_id: int, message: str, date: date):
        document = {"chat_id": chat_id, "message": message, "date": date}
        await spy.insert_one(document)
