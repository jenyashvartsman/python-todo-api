from fastapi import FastAPI
from todos_route import router

app = FastAPI()

app.include_router(router)
