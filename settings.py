from decouple import config


LOG_LEVEL = config('LOG_LEVEL')
REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')
EVENT_SERVICE_URL = config('EVENT_SERVICE_URL')