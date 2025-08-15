import os
from tavily import InvalidAPIKeyError, UsageLimitExceededError


from models import State
from common import query_db
from graph import tavily_client, load_url_content

os.environ["USER_AGENT"] = "Mozilla/5.0 (compatible; MyBot/1.0; +http://mywebsite.com/bot)"


def tavily_node(state:State):
    try:
        search_contents = list()
        query_db.update_one({"_id": state["query_id"]}, {"$set": {"status": "tavily searching"}})
        response = tavily_client.search(query=state.get("query"), max_results=5)
        if "results" in response and response["results"]:
            for index, result in enumerate(response["results"]):
                url = result.get("url", "")
                if url:
                    query_db.update_one({"_id": state["query_id"]}, {"$set": {"status": "Load blog contents"}})
                    content = load_url_content(url=url)
                    if content:
                        search_contents.append({
                            "title": result.get("title", ""),
                            "url": url,
                            "content": content,
                            "score": result.get("score", "")
                        })

                if search_contents:
                    break

        else:
            query_db.update_one({"_id": state["query_id"]}, {"$set": {"status": "No data found on tavily search"}})

    except (InvalidAPIKeyError, UsageLimitExceededError, Exception) as err:
        query_db.update_one({"_id": state["query_id"]}, {"$set": {"status": f"Tavily search failed:{err}"}})
        search_contents = list()

    return dict(search_contents=search_contents)

