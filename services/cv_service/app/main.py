from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="CV Service")

app.include_router(routes.router)
