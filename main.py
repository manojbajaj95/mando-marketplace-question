from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_db_and_tables
from routes import admin, companies, experts, marketplace

app = FastAPI()
app.include_router(admin.router)
app.include_router(companies.router)
app.include_router(experts.router)
app.include_router(marketplace.router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


@app.get("/")
def read_root():
    return {"Hello": "World"}
