from pymongo import MongoClient
from pydantic import BaseModel, EmailStr


class PayloadTemplate(BaseModel):
    query: str
    email: EmailStr


connection = MongoClient("mongodb://localhost:27017/")
database = connection["ShopGenie"]
query_db = database["query"]

