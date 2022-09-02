"""
Vault for the bot secrets and variables.
"""

from json import load


def get_bot_config(value: str) -> str:
    """
    Return a bot config value.
    """

    with open("config/settings.json", "r", encoding="utf8") as config:
        return load(config)[value]


def get_redis_config(value: str) -> str:
    """
    Return a Redis database config value.
    """

    with open("config/redis.json", "r", encoding="utf8") as config:
        return load(config)[value]
