from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .server.routers import gpus

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


app.include_router(gpus.router)


@app.get("/")
def get_root():
    return {"message": "This is a root"}
