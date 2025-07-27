from pymongo import MongoClient
from langchain_groq import ChatGroq
from typing_extensions import TypedDict
from pydantic import BaseModel, EmailStr
from googleapiclient.discovery import build


# Payload Validation
class PayloadTemplate(BaseModel):
    query: str
    email: EmailStr


class State(TypedDict):
    query: str
    email: str
    products: list[dict]
    youtube_link: str


# Database connection
connection = MongoClient("mongodb://localhost:27017/")
database = connection["ShopGenie"]
query_db = database["query"]

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key="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",
    temperature=0.5,
)

# youtube client
youtube = build('youtube', 'v3', developerKey="AIzaSyAB1x1renmmwO-l3T_r_AtkaUDj1LQxYTo")
