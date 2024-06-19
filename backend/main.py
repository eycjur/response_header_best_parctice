
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

todos = [
	"sample todo 1",
    "sample todo 2",
    "sample todo 3",
]

headers = {
    'Content-Security-Policy': "default-src 'self'; frame-ancestors 'none';",
    'Cross-Origin-Resource-Policy': 'same-origin',
    'X-Powered-By': "",
}

class TodoBody(BaseModel):
    todo: str

@app.get("/todos")
def read_todos() -> JSONResponse:
    return JSONResponse(content=todos, headers=headers)

@app.post("/todos")
def create_todos(body: TodoBody) -> JSONResponse:
    todos.append(body.todo)
    return JSONResponse(content={"message": "Todo created successfully!"}, headers=headers)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
