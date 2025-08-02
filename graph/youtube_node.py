from googleapiclient.discovery import build

# youtube client

from common import query_db
youtube = build('youtube', 'v3', developerKey="AIzaSyAB1x1renmmwO-l3T_r_AtkaUDj1LQxYTo")


def youtube_node(state):
    print("state: ", state)
    youtube_link = None
    best_product = state.get('best_product')
    if best_product:
        query_db.update_one({"_id": state["query_id"]},
                            {"$set": {
                                "status": "Youtube search in progresss",

                            }
                            })

        youtube_videos = youtube.search().list(
            q=f"{best_product['product_name']} review",
            part="snippet",
            type="video",
            maxResults=1
        ).execute()

        youtube_videos = youtube_videos.get("items", [])
        if youtube_videos:
            youtube_link = f"https://www.youtube.com/watch?v={youtube_videos[0]['id']['videoId']}"

    # query_db.update_one({"_id": state["query_id"]},
    #                     {"$set": {
    #                         "status": "Searching completed",
    #                         "products": state["products"],
    #                         "best_product": state["best_product"],
    #                         "youtube_link": youtube_link
    #
    #                     }
    #                     })

    return dict(youtube_link=youtube_link)





