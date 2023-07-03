from database import session
from todos_schema import Todo
from todos_dto import CreateTodoDto, UpdateTodoDto, TodoDto

# map todo to DTO
def todo_to_dto(todo) -> TodoDto:
    return TodoDto(id=todo.id, todo=todo.todo, completed=todo.completed)

# get all todos
async def get_todos() -> list[TodoDto]:
    todos_query = session.query(Todo)
    todos: list[Todo] = todos_query.all()
    return list(map(lambda todo: todo_to_dto(todo), todos))

# get one todo
async def get_todo(id: int) -> TodoDto | None:
    todos_query = session.query(Todo)
    todo = todos_query.get(id)
    return todo_to_dto(todo) if todo is not None else None

# create todo 
async def create_todo(todo: CreateTodoDto) -> TodoDto:
    new_todo = Todo(todo=todo.todo)

    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)
    
    return todo_to_dto(new_todo)

# update todo
async def update_todo(id: int, todo: UpdateTodoDto) -> TodoDto | None:
    todos_query = session.query(Todo)
    todo_update = todos_query.get(id)

    if todo_update is not None:
        todo_update.todo = todo.todo
        todo_update.completed = todo.completed
        session.commit()
        return todo_to_dto(todo_update)
    else:
        return None

# delete todo
async def delete_todo(id: int) -> TodoDto | None:
    todos_query = session.query(Todo)
    todo_delete = todos_query.get(id)
    
    if todo_delete is not None:
        todo_delete_dto = todo_to_dto(todo_delete)
        session.delete(todo_delete)
        session.commit()
        return todo_delete_dto
    else:
        return None

