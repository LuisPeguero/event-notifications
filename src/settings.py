from decouple import config


LOG_LEVEL = config('LOG_LEVEL', default='INFO')
REDIS_HOST = config('REDIS_HOST', default='localhost')
REDIS_PORT = config('REDIS_PORT', default=6379, cast=int)
EVENT_SERVICE_URL = config('EVENT_SERVICE_URL', default='http://localhost:5000')