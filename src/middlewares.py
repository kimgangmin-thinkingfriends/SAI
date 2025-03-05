from fastapi import Request, status
from fastapi.responses import JSONResponse

from config import get_settings

settings = get_settings()

async def add_check_api_key(request: Request, call_next):
    api_key = request.headers.get("X-API-KEY")
    if api_key != settings.api_key:
        return JSONResponse(content={"message": "접근 권한이 없습니다 (API 키)"}, status_code=status.HTTP_401_UNAUTHORIZED)
    response = await call_next(request)
    return response