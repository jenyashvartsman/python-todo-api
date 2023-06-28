from fastapi import FastAPI

from routes import todos_route

app = FastAPI()

app.include_router(todos_route.router)
