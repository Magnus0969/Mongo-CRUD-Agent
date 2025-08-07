from pymongo import MongoClient
from config import get_mongo_client
from typing import List, Dict, Any

class MongoCRUD:
    def __init__(self, db_name):
        self.client = get_mongo_client()
        self.db = self.client[db_name]

    def create(self, collection, data: dict):
        return self.db[collection].insert_one(data).inserted_id

    def read(self, collection, query: Dict[str, Any] = {}) -> List[Dict[str, Any]]:
        return list(self.db[collection].find(query))

    def update(self, collection, query: dict, new_values: dict):
        return self.db[collection].update_many(query, {"$set": new_values}).modified_count

    def delete(self, collection, query: dict):
        return self.db[collection].delete_many(query).deleted_count
