from fastapi import FastAPI
import logging

from data_abstraction import SingleText, MultiText
from model import translate
from remote_api import translate_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

@app.get('/')
def index():
    return {'message': ('Hello, If you are here it means you are lost. '
                        'See the "docs" endpoint for more info.')}

@app.get('/hello/{name}')
def hello_name_view(name: str = None, nickname: str = None):
    if not name:
        return {'message': 'Hello, no name provided to this curious endpoint.'}
    return {'message': (f'Hello {name}, this is a curious endpoint. '
                        f'Your nickname is {nickname}')}

@app.post('/echo')
def echo_view(text_to_translate: SingleText):
    local_translation = translate(text_to_translate.input_text)[0]
    remote_translation = translate_api(text_to_translate.input_text)[0]
    return {
        'message': text_to_translate.input_text,
        'local_translated_message' : local_translation,
        'remote_translated_message' : remote_translation,
    }

@app.post('/echoes')
def echo_view(texts_to_translate: MultiText):
    local_translations = translate(*texts_to_translate.input_texts)
    remote_translations = [translate_api(t)
                           for t in texts_to_translate.input_texts]
    return {
        'messages': texts_to_translate.input_texts,
        'local_translated_messages' : local_translations,
        'remote_translated_messages' : remote_translations,
    }


if __name__ == '__main__':
    logger.error('Start app server using main.py')
