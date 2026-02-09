from fastapi import FastAPI
from contextlib import asynccontextmanager
from uvicorn import run
from typing import Literal

from utils.logger import logger
from database import Model, engine
from routers.books import router as books_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        logger.info('Starting app...')
        await conn.run_sync(Model.metadata.create_all) # TODO: Сделать нормальные миграции с Alembic вместо .create_all
        logger.info('Database is ready to use')
        yield
        logger.info('Shutting down...')

app = FastAPI(
    title='LibraryAPI',
    description='API-сервис для онлайн-библиотеки',
    lifespan=lifespan
    )
app.include_router(books_router)



MODE: Literal['dev', 'prod'] = 'dev' # enter there the mode
# TODO: Вынести это в конфиги без хардкода

if MODE == 'dev':
    # dev/test mode
    if __name__ == '__main__':
        run(app='main:app',
            host='127.0.0.1',
            port=8000,
            reload=True,
            )
elif MODE == 'prod':
    # prod mode
    if __name__ == '__main__':
        run(app='main:app',
            host='0.0.0.0',
            port=8000,
            workers=4,
            )