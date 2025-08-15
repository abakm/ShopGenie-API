import uvicorn
from json import dumps
from threading import Thread
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware


from common import query_db
from models import PayloadTemplate
from graph.workflow import trigger_graph
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://shopgenie-ui-production.up.railway.app"],  # Your React app URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.post('/api/post')
def post(payload: PayloadTemplate):
    payload = payload.model_dump()
    query_ids = query_db.distinct("_id")
    query_id = max(query_ids)+1 if query_ids else 1
    query_db.insert_one(dict(_id=query_id, query=payload["query"], email=payload["email"], status="searching"))
    Thread(target=trigger_graph, args=(query_id, payload["query"], payload["email"])).start()
    return Response(
        content=dumps(dict(query_id=query_id)),
        status_code=200,
    )


@app.get('/api/get/{query_id}')
def get(query_id: int):
    query = query_db.find_one({"_id": query_id})
    status_code = 200 if query else 404
    return Response(
        content=dumps(query),
        status_code=status_code,
    )



if __name__ == '__main__':
    uvicorn.run(app,  host="0.0.0.0", port=5000)
