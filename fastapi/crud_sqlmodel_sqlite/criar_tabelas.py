from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from core.database import engine

async def create_tables(engine:AsyncEngine) -> None:
    import models.__all_model
    print('Criando as tabelas no banco de dados...')

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables(engine))