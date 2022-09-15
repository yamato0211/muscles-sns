from fastapi import FastAPI

app = FastAPI(
    title="muscles-backend"
)

@app.get("/")
async def hello():
    return {"message" : "Hello world!"}