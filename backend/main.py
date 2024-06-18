
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

todos = [
	"sample todo 1",
    "sample todo 2",
    "sample todo 3",
]

class TodoBody(BaseModel):
    todo: str

@app.get("/todos")
def read_todos() -> list[str]:
    return todos

@app.post("/todos")
def create_todos(body: TodoBody) -> dict[str, str]:
    todos.append(body.todo)
    return {"message": "Todo created successfully!"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
