import os
import asyncio
from dotenv import load_dotenv
from psycopg import AsyncConnection
from psycopg.rows import dict_row

load_dotenv()


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


async def get_connection() -> AsyncConnection:
    return await AsyncConnection.connect(DATABASE_URL, row_factory=dict_row)


async def create_table():
    conn = await get_connection()
    async with conn.cursor() as cursor:

        await cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS to_dos (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                is_completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )

    await conn.commit()
    await conn.close()


async def insert(title:str):
    name = title.capitalize()
    
    conn = await get_connection()
    async with conn.cursor() as cursor:

        await cursor.execute(
            """
            INSERT INTO to_dos (title)
            VALUES (%s)
            """, (name,)
            )

    await conn.commit()
    await conn.close()


async def complete(title:str):
    name = title.capitalize()

    conn = await get_connection()
    async with conn.cursor() as cursor:

        await cursor.execute(
            """
            UPDATE to_dos
            SET is_completed = TRUE
            WHERE title = (%s)
            """, (name,)
        )

    await conn.commit()
    await conn.close()


async def list_all():
    conn = await get_connection()
    async with conn.cursor() as cursor:

        await cursor.execute(
            """
            SELECT * FROM to_dos
            """
        )
        results = await cursor.fetchall()
        return results
    
    await conn.close()


async def search_by_name(title:str):
    name = title.capitalize()

    conn = await get_connection()
    async with conn.cursor() as cursor:

        await cursor.execute(
            """
            SELECT * FROM to_dos
            WHERE title = (%s)
            """, (name,)
        )
        results = await cursor.fetchall()
        return results
    
    await conn.close()


async def del_by_name(title:str):
    name = title.capitalize()

    conn = await get_connection()
    async with conn.cursor() as cursor:

        await cursor.execute(
            """
            DELETE FROM to_dos
            WHERE title = (%s)
            """, (name,)
        )
    await conn.commit()
    await conn.close()