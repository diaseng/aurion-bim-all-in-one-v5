
from fastapi import APIRouter
router = APIRouter()
@router.get("/ping")
def ping():
    return {"status":"ok","service":"aurion-api","version":"5.0"}
