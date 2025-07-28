from groq import Groq
from pymongo import MongoClient
from langchain_groq import ChatGroq
from typing_extensions import TypedDict
from googleapiclient.discovery import build
from langchain_community.document_loaders import WebBaseLoader

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
    model="llama3-70b-8192",
    api_key="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",
    temperature=0.5,
)

client = Groq(api_key="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")
models = client.models.list()
for model in models:
    print(model)

# youtube client
youtube = build('youtube', 'v3', developerKey="AIzaSyAB1x1renmmwO-l3T_r_AtkaUDj1LQxYTo")


def load_url_content(url: str):
    loader = WebBaseLoader(web_paths=[url], bs_get_text_kwargs={"separator": " ", "strip": True})
    documents = loader.load()
    documents = " ".join([document.page_content for document in documents])
    return documents