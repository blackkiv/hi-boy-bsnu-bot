from motor import motor_asyncio
from properties import MONGODB_HOST,MONGODB_PORT


class MessageRepository(object):
    def __init__(self):
        global mongo
        client = motor_asyncio.AsyncIOMotorClient(MONGODB_HOST, MONGODB_PORT)
        print(client.server_info())
        mongo = client["msg"]["messages"]

    async def save(self, chat_id: str, message: str):
        document = {"chat_id": chat_id, "message": message}
        await mongo.insert_one(document)

    async def get(self, chat_id: str):
        result = await mongo.find_one({"chat_id": chat_id})
        return result["message"]

    async def delete(self, chat_id: int):
        await mongo.delete_many({"chat_id": chat_id})
