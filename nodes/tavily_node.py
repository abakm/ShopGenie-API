import os
from tavily import TavilyClient, InvalidAPIKeyError, UsageLimitExceededError

from common import load_url_content
os.environ["USER_AGENT"] = "Mozilla/5.0 (compatible; MyBot/1.0; +http://mywebsite.com/bot)"

from common import query_db

# Tavily for web search
tavily_client = TavilyClient(api_key="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")


def tavily_node(query_data):

    try:
        search_contents = list()
        response = tavily_client.search(query=query_data.get("query"), max_results=1)
        if "results" in response and response["results"]:
            for result in response["results"]:
                url = result.get("url", "")
                if url:
                    content = load_url_content(url=url)
                    if content:
                        search_contents.append({
                            "title": result.get("title", ""),
                            "url": url,
                            "content": content,
                            "score": result.get("score", "")
                        })

    except (InvalidAPIKeyError, UsageLimitExceededError, Exception) as err:
        search_contents = list()

    return dict(search_contents=search_contents)

