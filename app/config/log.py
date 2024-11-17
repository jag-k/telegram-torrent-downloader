import logging

from .settings import APP_NAME


__all__ = ("logger",)

logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)
