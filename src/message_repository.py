from elasticsearch import AsyncElasticsearch
from properties import ELASTICSEARCH_HOST


class MessageRepository(object):
    def __init__(self):
        global es
        es = AsyncElasticsearch(hosts=[{"host": ELASTICSEARCH_HOST}])

    async def save(self, chat_id: str, message: str):
        index = f"bot{chat_id}"
        await es.index(index, id=chat_id, body={"msg": message})

    async def get(self, chat_id: int):
        index = f"bot{chat_id}"
        res = await es.get(index, id=chat_id)
        return res["_source"]["msg"]

    async def delete(self, chat_id: int):
        index = f"bot{chat_id}"
        await es.delete(index, id=chat_id)
