import uvicorn  

from logger import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.controllers import register_controllers
from settings import LOG_LEVEL


logger.info("Starting the server")

app = FastAPI(title='api', docs_url=None, redoc_url="/docs")
register_controllers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
)


if __name__ == '__main__': 
    uvicorn.run(app, reload=True, port=5000, log_level=LOG_LEVEL)