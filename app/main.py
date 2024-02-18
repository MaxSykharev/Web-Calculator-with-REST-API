from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.backend.api.routes import router

app = FastAPI()

app.include_router(router)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)