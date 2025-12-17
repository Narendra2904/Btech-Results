# config/settings.py

# Redis cache expiry time (in seconds)
# 24 hours = 60 * 60 * 24
EXPIRY_TIME = 60 * 60 * 24

# Redis connection settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None   # keep None if no password
