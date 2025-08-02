from models import State
from common import query_db


def store_node(state:State):
    query_db.update_one({"_id": state["query_id"]},
                        {"$set": {
                            "status": "Searching completed",
                            "products": state["products"],
                            "best_product": state["best_product"],
                            "youtube_link": state["youtube_link"]

                        }
                        })