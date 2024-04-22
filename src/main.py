import traceback
import uuid

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from api.dependencies import bearer_token
from api.v1.routers import router as v1_api_router
from core.config import settings
from models.token_model import TokenModel

app = FastAPI()

app.mount(
    "/static", StaticFiles(directory=settings.static_files_path), name="static"
)
app.include_router(v1_api_router, prefix="/api/v1")


@app.exception_handler(Exception)
async def error_handler(_: Request, exc: Exception):
    custom_message = "An error occurred: {}".format(str(exc))
    traceback_message = traceback.format_exc()
    return JSONResponse(
        status_code=500,
        content={"message": custom_message, "traceback": traceback_message},
    )


@app.get("/link/{link_id}")
async def make_click(
    link_id: uuid.UUID 
):
    return RedirectResponse(url=f"/api/v1/links/click/{link_id}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        ssl_keyfile=f"{settings.certificates_path}/key.pem",
        ssl_certfile=f"{settings.certificates_path}/cert.pem",
        reload=True,
    )
