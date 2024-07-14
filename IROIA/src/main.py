from fastapi import FastAPI
from .data.database import engine, Base
from .data.dependency import init_db, get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .model import model
app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()

@app.get("/")
async def hello():
    return {"hello"}


@app.get("/hi")
async def name(db: AsyncSession = Depends(get_db)):
    file = await db.execute(select(model.User))
    data = file.scalar()
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return data

