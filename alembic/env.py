import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.config import settings
from app.database import Base

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_offline():
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = create_async_engine(settings.DATABASE_URL, echo=True)

    async def do_run_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(target_metadata.create_all)
            await context.run_migrations()

    asyncio.run(do_run_migrations())

    context.configure(
        connection=connectable,
        target_metadata=target_metadata,
    )

    if context.is_offline_mode():
        run_migrations_offline()
    else:
        run_migrations_online()


