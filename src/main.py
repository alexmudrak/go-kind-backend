import traceback

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

from api.v1.routers import router as v1_api_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(v1_api_router, prefix="/api/v1")


@app.exception_handler(Exception)
async def error_handler(_: Request, exc: Exception):
    custom_message = "An error occurred: {}".format(str(exc))
    traceback_message = traceback.format_exc()
    return JSONResponse(
        status_code=500,
        content={"message": custom_message, "traceback": traceback_message},
    )


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/logout")
async def logout(request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        ssl_keyfile="./certificates/key.pem",
        ssl_certfile="./certificates/cert.pem",
    )
