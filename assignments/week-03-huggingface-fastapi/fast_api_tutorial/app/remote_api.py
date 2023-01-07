import logging
import re
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


raw_token = open('../../.env').read()
token = re.match(r'.*"(.*)"$', raw_token).group(1)
API_URL = 'https://api-inference.huggingface.co/models/t5-small'
headers = {'Authorization': 'Bearer ' + token}

def translate_api(text):
    payload = {'inputs': text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == '__main__':
    logger.error('Start app server using main.py')
