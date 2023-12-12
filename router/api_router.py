from fastapi import APIRouter

from api.api_file_to_text import router as api_file_to_text_router

api_router = APIRouter()

api_router.include_router(api_file_to_text_router, tags=["file_to_text"], prefix="/file_to_text")

