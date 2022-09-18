import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.models import Base
from db.database import engine
from routers.main import router
import uvicorn

Base.metadata.create_all(bind=engine)
PORT = os.environ.get("PORT",8000)

app = FastAPI(
    title="muscles-backend"
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health():
    return {"message" : "Hello world!"}

app.include_router(router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=PORT)