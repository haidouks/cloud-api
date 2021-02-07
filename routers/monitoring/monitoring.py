from fastapi import APIRouter
from .base_models import OUTHealth

router = APIRouter()  
  
@router.get("/health", response_model=OUTHealth,tags=["monitoring"])
async def get_api_health():
  result = {
      "status" : "up"
  }
  return result