"""
Database functions module.
"""

from aioredis import Redis, ConnectionPool

# pylint: disable=broad-except


def return_redis_instance(
    host: str = "localhost",
    port: int = 6379,
    username: str = None,
    password: str = None,
    database: int = 0
) -> Redis:
    """
    Create and return a Redis instance
    """

    pool = ConnectionPool.from_url(
        f"redis://{host}:{port}/{database}",
        max_connections=2,
    )
    return Redis(
        connection_pool=pool,
        username=username,
        password=password
    )

# money functions

async def get_money(redis_ins: Redis, user_id: int):
    """
    Get money with the given user_id
    """

    return await redis_ins.hget("money", user_id)

async def set_money(redis_ins: Redis, user_id: int, value: int):
    """
    Set money with the given user_id and value
    """

    return await redis_ins.hset("money", user_id, value)

async def del_money(redis_ins: Redis, user_id: int):
    """
    Delete user money with given user_id
    """

    return await redis_ins.hdel("money", user_id)
