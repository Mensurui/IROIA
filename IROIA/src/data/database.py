from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase

database_name = "Import ROI Analysis"
DATABASE_URL = f"postgresql+asyncpg://iroia:mensur@127.0.0.1/{database_name}"

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = async_sessionmaker(engine,class_=AsyncSession)

class Base(DeclarativeBase):
    pass
