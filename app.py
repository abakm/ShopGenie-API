import uvicorn
from json import dumps
from fastapi import FastAPI, Response

from common import PayloadTemplate, query_db

app = FastAPI()


@app.post('/api/post')
def search(payload: PayloadTemplate):
    payload = payload.model_dump()
    query_ids = query_db.distinct("_id")
    query_id = max(query_ids)+1 if query_ids else 1
    query_db.insert_one(dict(_id=query_id, query=payload["query"], email=payload["email"], status="searching",
                             result=None))

    return Response(
        content=dumps(dict(query_id=query_id)),
        status_code=200,
    )


@app.post('/api/get/{query_id}')
def get(query_id: int):
    print(query_id)
    query = query_db.find_one({"_id": query_id})
    status_code = 200 if query else 404
    return Response(
        content=dumps(query),
        status_code=status_code,
    )


if __name__ == '__main__':
    uvicorn.run(app,  host="0.0.0.0", port=5000)
