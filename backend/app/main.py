from fastapi import FastAPI
from backend.app.routes import router
from backend.app.database import engine, Base
from backend.app import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
