from fastapi import FastAPI
from app.database import init_db
from app.events import init_queues
from app.routers import atelier_router


service_name = "Atelier"
app = FastAPI(title=service_name)


@app.on_event("startup")
async def startup():
    # create db tables
    await init_db()
    init_queues()


app.include_router(atelier_router, tags=["Atelier"], prefix="/api/v1/atelier")
