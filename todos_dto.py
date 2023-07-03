from pydantic import BaseModel

class CreateTodoDto(BaseModel):
    todo: str

class UpdateTodoDto(CreateTodoDto):
    completed: bool

class TodoDto(UpdateTodoDto):
    id: int