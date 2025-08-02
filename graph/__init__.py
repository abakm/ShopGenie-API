from tavily import TavilyClient
from langchain_groq import ChatGroq
from googleapiclient.discovery import build
from langchain_community.document_loaders import WebBaseLoader

llm = ChatGroq(
    model="llama3-70b-8192",
    api_key="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",
    temperature=0.5,
)

# tavily for web search
tavily_client = TavilyClient(api_key="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")

youtube = build('youtube', 'v3', developerKey="AIzaSyAB1x1renmmwO-l3T_r_AtkaUDj1LQxYTo")


def load_url_content(url: str):
    loader = WebBaseLoader(web_paths=[url], bs_get_text_kwargs={"separator": " ", "strip": True})
    documents = loader.load()
    documents = " ".join([document.page_content for document in documents])
    return documents

