from fastapi import FastAPI

app = FastAPI()


@app.get("/todos")
async def get_todos():
    return "get todos"


@app.get("/todos/{id}")
async def get_todo():
    return "get tod"


@app.post("/todos")
async def create_todo():
    return "create todo"


@app.put("/todos/{id}")
async def update_todo():
    return "update todo"


@app.delete("/todos/{id}")
async def delete_todo():
    return "delete todo"


@app.put("/todos/{id}/complete")
async def complete_todo():
    return "complete todo"
