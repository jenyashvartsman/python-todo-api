
from fastapi import APIRouter, HTTPException
from todos_dto import CreateTodoDto, UpdateTodoDto
import todos_crud

router = APIRouter()

# 404, todo not found exception
def todo_not_found(id: int):
    raise HTTPException(status_code=404, detail=f'todo with id {id} was not found')

# get all todos
@router.get("/todos")
async def get_todos():
    return await todos_crud.get_todos()

# get one todo
@router.get("/todos/{id}")
async def get_todo(id):
    todo = await todos_crud.get_todo(id)
    return todo if todo is not None else todo_not_found(id)

# create todo
@router.post("/todos")
async def create_todo(todo: CreateTodoDto):
    return await todos_crud.create_todo(todo)

# update todo
@router.put("/todos/{id}")
async def update_todo(id: int, todo: UpdateTodoDto):
    todo = await todos_crud.update_todo(id, todo)
    return todo if todo is not None else todo_not_found(id)

# delete todo
@router.delete("/todos/{id}")
async def delete_todo(id: int):
    todo = await todos_crud.delete_todo(id)
    return todo if todo is not None else todo_not_found(id)
