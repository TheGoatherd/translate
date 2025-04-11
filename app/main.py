from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import app_router

app = FastAPI(title="translate")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(app_router)

# Default route
@app.get("/")
async def root():
    return {"message": "Ye toh shikhar ka final year project hai bhai!"}
