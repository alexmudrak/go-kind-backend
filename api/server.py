from fastapi import Depends,status, FastAPI, Request, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import traceback
from fastapi import FastAPI, Depends, HTTPException
from authlib.integrations.starlette_client import OAuth
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


app_key="uHHX7LXWnshmoHlgGkmpBeIzP"
app_secret="tHldeDxrOUdtT8FtN2q6vzTtCrwmFWBooRayFaZUWiBmJEP1am"

access_token="1755669308997259264-l4dctliLMuzVmG2BCsWaMm6VLmutpf"
access_token_secret="EYiWL9qdS13TUMt512Ek9lKnWyUpBstSyoFjKQg1SA3X6"

client_id="N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ"
client_secret="JMLkZIaNg-IcmlrxzYucfxHzjfGS1En4oe1j2-HCTTfD8-4ypC",




oauth = OAuth()
oauth.register(
    'twitter',
    client_id=client_id,
    client_secret=client_secret,
    authorize_url='https://twitter.com/i/oauth2/authorize',
    authorize_params=None,
    access_token_url='https://api.twitter.com/oauth2/token',
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='YOUR_CALLBACK_URL',
    client_kwargs={'scope': 'tweet.read users.read'},
)


from fastapi import FastAPI, Request
import httpx

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret-string")

redirect_uri = "https://gokind.xyz/authorize/twitter"

@app.exception_handler(Exception)
async def error_handler(request: Request, exc: Exception):
    custom_message = "An error occurred: {}".format(str(exc))
    traceback_message = traceback.format_exc()
    return JSONResponse(
        status_code=500,
        content={"message": custom_message, "traceback": traceback_message}
    )


@app.get("/")
def read_root():
    return FileResponse('index.html')

# Flask route to redirect user to Twitter's authorization page
@app.get("/login/twitter")
async def login_twitter():
    # Redirect user to Twitter's OAuth 2.0 authorization page
    auth_url = f'''https://twitter.com/i/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=tweet.read%20users.read%20follows.read%20follows.write&state=state&code_challenge=challenge&code_challenge_method=plain'''
    return RedirectResponse(url=auth_url)


#@app.route("/authorize/twitter")
#async def authorize_twitter(data):
#    token = data.query_params['code']
#    token = await oauth.twitter.authorize_access_token()
#    #resp = await oauth.twitter.get('account/verify_credentials.json', token=token)
#    #user_info = resp.json()
#    # Use user_info according to your application's needs
#    print(token)
#    return token


@app.get('/authorize/twitter')
async def auth(request: Request):
    token = await oauth.twitter.authorize_access_token(request)
    url = 'account/verify_credentials.json'
    resp = await oauth.twitter.get(
        url, params={'skip_status': True}, token=token)
    user = resp.json()
    request.session['user'] = dict(user)
    print(user)
    return RedirectResponse(url='/')


@app.get('/logout')
async def logout(request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
