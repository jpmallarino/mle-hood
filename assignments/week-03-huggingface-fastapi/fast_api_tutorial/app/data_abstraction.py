import logging
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SingleText(BaseModel):
    """Data point for a single prediction"""
    input_text: str = 'No text provided :('


class MultiText(BaseModel):
    """Data point for a multiple prediction"""
    input_texts: list[str] = ['No text provided :(']

if __name__ == '__main__':
    logger.error('Start app server using main.py')
