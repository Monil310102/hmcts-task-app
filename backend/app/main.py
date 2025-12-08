from fastapi import FastAPI
from app.routes import router
from app.database import engine, Base
from app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
