from datetime import datetime

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uvicorn

from middlewares import add_check_api_key
from config import get_settings
from routers.relighting_router import router as relighting_router
from container import Container

settings = get_settings()

app = FastAPI()

app.container = Container()

app.middleware("http")(add_check_api_key)

app.include_router(relighting_router)


@app.get("/")
def healthcheck():
    return JSONResponse(
        content={
            "message": "ok",
            "current_datetime": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
        },
        status_code=status.HTTP_200_OK,
    )


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
