async def get_todos():
    return "get todos"


async def get_todo(id):
    return f"get todo {id}"


async def create_todo():
    return "create todo"


async def update_todo(id):
    return "update todo {}".format(id)


async def delete_todo(id):
    return "delete todo {}".format(id)


async def complete_todo(id):
    return "complete todo {}".format(id)
