import logging
import sys

logger = logging.getLogger('APILogger')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

format = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s: %(message)s")
handler.setFormatter(format)

logger.handlers.clear()
logger.addHandler(handler)
logger.propagate = False