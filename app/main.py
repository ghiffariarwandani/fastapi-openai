from fastapi import FastAPI

from app.modules.coffee.router import coffee_router

app = FastAPI()
app.include_router(router=coffee_router)
