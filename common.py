from pymongo import MongoClient
# Database connection
connection = MongoClient("mongodb://localhost:27017/")
database = connection["ShopGenie"]
query_db = database["query"]



def load_url_content(url: str):
    loader = WebBaseLoader(web_paths=[url], bs_get_text_kwargs={"separator": " ", "strip": True})
    documents = loader.load()
    documents = " ".join([document.page_content for document in documents])
    return documents


