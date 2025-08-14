from pymongo import MongoClient
from typing_extensions import TypedDict
from langchain_community.document_loaders import WebBaseLoader

class State(TypedDict):
    query: str
    email: str
    products: list[dict]
    youtube_link: str

# Database connection
connection = MongoClient("mongodb+srv://shopgenie:shopgenie@cluster0.2zydot4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
database = connection["ShopGenie"]
query_db = database["query"]



def load_url_content(url: str):
    loader = WebBaseLoader(web_paths=[url], bs_get_text_kwargs={"separator": " ", "strip": True})
    documents = loader.load()
    documents = " ".join([document.page_content for document in documents])
    return documents