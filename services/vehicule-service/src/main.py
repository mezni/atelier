from fastapi import FastAPI
from app.database import init_db
#from app.events import init_queues
from app.routers import moteur_router, marque_router, categorie_router


service_name = "Vehicule"
app = FastAPI(title=service_name)


@app.on_event("startup")
async def startup():
    # create db tables
    await init_db()


app.include_router(moteur_router, tags=["Moteur"], prefix="/api/v1/vehicule")
app.include_router(categorie_router, tags=["Categorie"], prefix="/api/v1/vehicule")
app.include_router(marque_router, tags=["Marque"], prefix="/api/v1/vehicule")
