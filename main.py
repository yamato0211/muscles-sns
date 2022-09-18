from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.models import Base
from db.database import engine
from routers.main import router


Base.metadata.create_all(bind=engine)


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

