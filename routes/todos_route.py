
from fastapi import APIRouter
from crud import todos_crud

router = APIRouter()

@router.get("/todos")
async def get_todos():
    return await todos_crud.get_todos()


@router.get("/todos/{id}")
async def get_todo(id):
    return await todos_crud.get_todo(id)


@router.post("/todos")
async def create_todo():
    return await todos_crud.create_todo()


@router.put("/todos/{id}")
async def update_todo(id):
    return await todos_crud.update_todo(id)


@router.delete("/todos/{id}")
async def delete_todo(id):
    return await todos_crud.delete_todo(id)


@router.put("/todos/{id}/complete")
async def complete_todo(id):
    return await todos_crud.complete_todo(id)