from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import database
from routes import admin, companies, experts, marketplace

app = FastAPI()
app.include_router(admin.router)
app.include_router(companies.router)
app.include_router(experts.router)
app.include_router(marketplace.router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}
