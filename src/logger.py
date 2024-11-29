import sys
import logging

from settings import LOG_LEVEL

LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}

level = LOG_LEVELS.get(LOG_LEVEL, logging.INFO)
print(f"Log level: {level}")
logger = logging.getLogger(__name__)
logger.setLevel(level)
formatter = logging.Formatter(("%(asctime)s [%(processName)s: %(process)d]" 
                              "[%(threadName)s: %(thread)d] [%(levelname)s]"
                              " %(name)s: %(message)s"))

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)