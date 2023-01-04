from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def hello_name_view(name: str, last_name: str = None):
    return {"message": f"Hello {name}. Your last name is {last_name}"}


if __name__ == "__main__":
    logger.error("Start app server using main.py")
