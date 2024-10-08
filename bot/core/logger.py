import logging
from sys import stdout

logger = logging.getLogger("exchange_rate_bot")
logger.propagate = False
logger.setLevel(logging.DEBUG)
log_handler = logging.StreamHandler(stdout)
log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("[%(asctime)s] - %(levelname)s - %(name)s - %(message)s")
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
