from app.routers import prioritization
from app.routers import exposure
from app.database import Base, engine
from app.models.exposure import Exposure
from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CTEM Service",
    version="1.0.0"
)
app.include_router(exposure.router)
app.include_router(prioritization.router)

@app.get("/")
def home():

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "message": "MySQL Connected Successfully!"
    }