# config/redisConnection.py

import redis
from config.settings import (
    REDIS_HOST,
    REDIS_PORT,
    REDIS_DB,
    REDIS_PASSWORD,
)

class RedisConnection:
    def __init__(self):
        try:
            self.client = redis.Redis(
                host=REDIS_HOST,
                port=REDIS_PORT,
                db=REDIS_DB,
                password=REDIS_PASSWORD,
                decode_responses=True
            )
            # Test connection
            self.client.ping()
            print("✅ Redis connected")
        except Exception as e:
            print("❌ Redis not connected:", e)
            self.client = None

# Singleton instance (IMPORTANT)
redisConnection = RedisConnection()
