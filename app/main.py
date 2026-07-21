from app.routers import prioritization
from app.routers import exposure
from app.database import Base, engine
from app.models.exposure import Exposure
from fastapi import FastAPI
from sqlalchemy import text
from app.models.validation_plan import ValidationPlan
from app.routers import validation_plan
from app.database import engine
from app.routers import validation_schedule
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CTEM Service",
    version="1.0.0"
)
app.include_router(exposure.router)
app.include_router(prioritization.router)
app.include_router(validation_plan.router)
app.include_router(validation_schedule.router)

@app.get("/")
def home():

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "message": "MySQL Connected Successfully!"
    }