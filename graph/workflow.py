from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

from models import State
from graph.email_node import email_node
from graph.store_node import store_node
from graph.tavily_node import tavily_node
from graph.youtube_node import youtube_node
from graph.extraction_node import extraction_node
from graph.comparion_code import comparison_node

builder = StateGraph(State)
builder.add_node("tavily", tavily_node)
builder.add_node("extraction", extraction_node)
builder.add_node("comparison", comparison_node)
builder.add_node("youtube", youtube_node)
builder.add_node("email", email_node)
builder.add_node("store", store_node)

# Define edges to control flow between nodes
builder.add_edge(START, "tavily")
builder.add_edge("tavily", "extraction")
builder.add_edge("extraction", "comparison")
builder.add_edge("comparison", "youtube")
# builder.add_edge("youtube", END)

builder.add_edge("youtube", "store")
builder.add_edge("store", END)

builder.add_edge("youtube", "email")
builder.add_edge("email", END)

# Compile and display graph as Mermaid diagram
graph = builder.compile()
display(Image(graph.get_graph().draw_mermaid_png()))


def trigger_graph(query_id: int, query: str, email: str):
    for event in graph.stream(input=dict(query_id=query_id, query=query, email=email), stream_mode="updates"):
        print(event)


# initial_state = {"query_id": 1, "query": "Best smartphones under $10000", "email": "akhilakmgb@gmail.com"}
#
# for event in graph.stream(input=initial_state, stream_mode="updates"):
#     print(event)
