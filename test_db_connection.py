import asyncio
import asyncpg

async def test_connection():
    try:
        conn = await asyncpg.connect(
            user='fastapi_user',
            password='fastapi_password',
            database='fastapi_db',
            host='db'
        )
        print("Connection successful")
        await conn.close()
    except Exception as e:
        print(f"Error: {e}")

asyncio.run(test_connection())
