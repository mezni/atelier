from fastapi import APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app import schemas, repositories

moteur_router = APIRouter()

@moteur_router.get("/moteur/{id}", status_code=status.HTTP_200_OK)
async def get_moteur(id: int, session: AsyncSession = Depends(get_session)):
    entity_name = "moteur"
    msg_does_not_exists = entity_name+" n'existe pas"

    result = await repositories.get_moteur_by_id(session=session, id=id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=msg_does_not_exists)
    return result

@moteur_router.get("/moteur", status_code=status.HTTP_200_OK)
async def get_moteurs(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    result = await repositories.get_moteur_all(session=session, skip=skip, limit=limit)
    return result

@moteur_router.post("/moteur", status_code=status.HTTP_201_CREATED)
async def create_moteur(payload: schemas.MoteurCreate, session: AsyncSession = Depends(get_session)):
    entity_name = "moteur"
    msg_already_exists = entity_name+" existe deja"
    db_item = await repositories.get_moteur_by_name(session=session, name=payload.moteur)
    if db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=msg_already_exists)    
    result = await repositories.create_moteur(
        session=session, payload=payload.dict())
    return result


@moteur_router.put("/moteur/{id}", status_code=status.HTTP_200_OK)
async def update_moteur(id: int,payload: schemas.MoteurUpdate, session: AsyncSession = Depends(get_session)):
    entity_name = "moteur"
    msg_does_not_exists = entity_name+" n'existe pas"
    db_item = await repositories.get_moteur_by_id(session=session, id=id)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="moteur n'existe pas")
    result = await repositories.update_moteur(
        session=session, id=id, payload=payload.dict())
    return result

@moteur_router.delete("/moteur/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_moteur(id: int, session: AsyncSession = Depends(get_session)):
    entity_name = "moteur"
    msg_does_not_exists = entity_name+" n'existe pas"
    db_item = await repositories.get_moteur_by_id(session=session, id=id)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=msg_does_not_exists)
    result = await repositories.delete_moteur(
        session=session, id=id)
    return result

@moteur_router.get("/moteur/search/", status_code=status.HTTP_200_OK)
async def search_moteur(name: str, session: AsyncSession = Depends(get_session)):
    result = await repositories.search_moteur(
        session=session, name=name)
    return result 


marque_router = APIRouter()

@marque_router.get("/marque/{id}", status_code=status.HTTP_200_OK)
async def get_marque(id: int, session: AsyncSession = Depends(get_session)):
    entity_name = "marque"
    msg_does_not_exists = entity_name+" n'existe pas"

    result = await repositories.get_marque_by_id(session=session, id=id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=msg_does_not_exists)
    return result

@marque_router.get("/marque", status_code=status.HTTP_200_OK)
async def get_marques(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    result = await repositories.get_marque_all(session=session, skip=skip, limit=limit)
    return result

@marque_router.post("/marque", status_code=status.HTTP_201_CREATED)
async def create_marque(payload: schemas.MarqueCreate, session: AsyncSession = Depends(get_session)):
    entity_name = "marque"
    msg_already_exists = entity_name+" existe deja"
    db_item = await repositories.get_marque_by_name(session=session, name=payload.marque)
    if db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=msg_already_exists)    
    result = await repositories.create_marque(
        session=session, payload=payload.dict())
    return result


@marque_router.put("/marque/{id}", status_code=status.HTTP_200_OK)
async def update_marque(id: int,payload: schemas.MarqueUpdate, session: AsyncSession = Depends(get_session)):
    entity_name = "marque"
    msg_does_not_exists = entity_name+" n'existe pas"
    db_item = await repositories.get_marque_by_id(session=session, id=id)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="marque n'existe pas")
    result = await repositories.update_marque(
        session=session, id=id, payload=payload.dict())
    return result

@marque_router.delete("/marque/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_marque(id: int, session: AsyncSession = Depends(get_session)):
    entity_name = "marque"
    msg_does_not_exists = entity_name+" n'existe pas"
    db_item = await repositories.get_marque_by_id(session=session, id=id)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=msg_does_not_exists)
    result = await repositories.delete_marque(
        session=session, id=id)
    return result

@marque_router.get("/marque/search/", status_code=status.HTTP_200_OK)
async def search_marque(name: str, session: AsyncSession = Depends(get_session)):
    result = await repositories.search_marque(
        session=session, name=name)
    return result 



categorie_router = APIRouter()

@categorie_router.get("/categorie/{id}", status_code=status.HTTP_200_OK)
async def get_categorie(id: int, session: AsyncSession = Depends(get_session)):
    entity_name = "categorie"
    msg_does_not_exists = entity_name+" n'existe pas"

    result = await repositories.get_categorie_by_id(session=session, id=id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=msg_does_not_exists)
    return result

@categorie_router.get("/categorie", status_code=status.HTTP_200_OK)
async def get_categories(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)):
    result = await repositories.get_categorie_all(session=session, skip=skip, limit=limit)
    return result

@categorie_router.post("/categorie", status_code=status.HTTP_201_CREATED)
async def create_categorie(payload: schemas.CategorieCreate, session: AsyncSession = Depends(get_session)):
    entity_name = "categorie"
    msg_already_exists = entity_name+" existe deja"
    db_item = await repositories.get_categorie_by_name(session=session, name=payload.categorie)
    if db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=msg_already_exists)    
    result = await repositories.create_categorie(
        session=session, payload=payload.dict())
    return result


@categorie_router.put("/categorie/{id}", status_code=status.HTTP_200_OK)
async def update_categorie(id: int,payload: schemas.CategorieUpdate, session: AsyncSession = Depends(get_session)):
    entity_name = "categorie"
    msg_does_not_exists = entity_name+" n'existe pas"
    db_item = await repositories.get_categorie_by_id(session=session, id=id)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="categorie n'existe pas")
    result = await repositories.update_categorie(
        session=session, id=id, payload=payload.dict())
    return result

@categorie_router.delete("/categorie/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_categorie(id: int, session: AsyncSession = Depends(get_session)):
    entity_name = "categorie"
    msg_does_not_exists = entity_name+" n'existe pas"
    db_item = await repositories.get_categorie_by_id(session=session, id=id)
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=msg_does_not_exists)
    result = await repositories.delete_categorie(
        session=session, id=id)
    return result

@categorie_router.get("/categorie/search/", status_code=status.HTTP_200_OK)
async def search_categorie(name: str, session: AsyncSession = Depends(get_session)):
    result = await repositories.search_categorie(
        session=session, name=name)
    return result 

