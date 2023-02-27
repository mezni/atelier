
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func

from app import models


async def get_moteur_by_id(session: AsyncSession, id: int):
    q = await session.execute(select(models.Moteur).where(models.Moteur.id == id))
    return q.scalars().first()

async def get_moteur_by_name(session: AsyncSession, name: str):
    q = await session.execute(select(models.Moteur).where(func.lower(models.Moteur.moteur) == func.lower(name)))
    return q.scalars().first()

async def get_moteur_all(session: AsyncSession, skip: int, limit: int):
    q = await session.execute(select(models.Moteur))
    result = q.scalars().all()
    return result[skip:limit+skip]

async def create_moteur(session: AsyncSession, payload: dict):
    item_db=models.Moteur(**payload)
    session.add(item_db)
    await session.commit()
    await session.refresh(item_db)
    return item_db

async def update_moteur(session: AsyncSession, id: int, payload: dict):
    db_item = await get_moteur_by_id(session=session, id=id)
    if payload:
        payload_data = dict([(k, v) for k, v in payload.items() if (v)])
        for key, value in payload_data.items():
            setattr(db_item, key, value)
        session.add(db_item)
        await session.commit()
        await session.refresh(db_item)
        return db_item   

async def delete_moteur(session: AsyncSession, id: int):
    db_item = await get_moteur_by_id(session=session, id=id)
    await session.delete(db_item)
    await session.commit()
    return {"status": "deleted"}

async def search_moteur(session: AsyncSession, name: str):
    if name != "":
        q = await session.execute(select(models.Moteur).where(func.lower(models.Moteur.moteur).like(func.lower('%'+name+'%'))))
    return q.scalars().all()


async def get_marque_by_id(session: AsyncSession, id: int):
    q = await session.execute(select(models.Marque).where(models.Marque.id == id))
    return q.scalars().first()

async def get_marque_by_name(session: AsyncSession, name: str):
    q = await session.execute(select(models.Marque).where(func.lower(models.Marque.marque) == func.lower(name)))
    return q.scalars().first()

async def get_marque_all(session: AsyncSession, skip: int, limit: int):
    q = await session.execute(select(models.Marque))
    result = q.scalars().all()
    return result[skip:limit+skip]

async def create_marque(session: AsyncSession, payload: dict):
    item_db=models.Marque(**payload)
    session.add(item_db)
    await session.commit()
    await session.refresh(item_db)
    return item_db

async def update_marque(session: AsyncSession, id: int, payload: dict):
    db_item = await get_marque_by_id(session=session, id=id)
    if payload:
        payload_data = dict([(k, v) for k, v in payload.items() if (v)])
        for key, value in payload_data.items():
            setattr(db_item, key, value)
        session.add(db_item)
        await session.commit()
        await session.refresh(db_item)
        return db_item   

async def delete_marque(session: AsyncSession, id: int):
    db_item = await get_marque_by_id(session=session, id=id)
    await session.delete(db_item)
    await session.commit()
    return {"status": "deleted"}

async def search_marque(session: AsyncSession, name: str):
    if name != "":
        q = await session.execute(select(models.Marque).where(func.lower(models.Marque.marque).like(func.lower('%'+name+'%'))))
    return q.scalars().all()

