import logging
from transformers import pipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

__all__ = ['translate']


# NOTE: Preloading the model to avoid latency on the first request
_translator = pipeline('translation_en_to_fr',
                             model='model/trans-1')

def translate(*text):
    return _translator(list(text))


if __name__ == '__main__':
    logger.error('Start app server using main.py')
