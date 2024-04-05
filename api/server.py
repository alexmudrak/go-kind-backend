import traceback

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from starlette.responses import RedirectResponse
from utils.auth_helper import TwitterWrapper

app = FastAPI()
twitter = TwitterWrapper()


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
    return FileResponse("index.html")


@app.get("/login/twitter")
async def login_twitter():
    authorize_url = twitter.get_authorization_url()
    return RedirectResponse(url=authorize_url)


@app.get("/authorize/twitter")
async def authorize_twitter(request: Request):
    url = str(request.url)
    access_token = twitter.get_access_token(url)

    return access_token


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
        ssl_keyfile="key.pem",
        ssl_certfile="cert.pem",
    )
