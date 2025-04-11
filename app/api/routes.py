from fastapi import APIRouter
from .endpoints import chutpaglu 

app_router = APIRouter()

app_router.post("/chutpaglu")(chutpaglu)