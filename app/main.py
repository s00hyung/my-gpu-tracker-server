from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from .server.routers import gpus, price
from .server.tasks import crawler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


app.include_router(gpus.router)
app.include_router(price.router)


async def start_crawling():
    await crawler.start()


@app.get("/", tags=["root"])
def get_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(start_crawling)
    return {"message": "This is a root"}
