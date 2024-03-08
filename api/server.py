from fastapi import Depends,status, FastAPI, Request, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import traceback
from fastapi import FastAPI, Depends, HTTPException
from authlib.integrations.starlette_client import OAuth
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


client_id="N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ"
client_secret="JMLkZIaNg-IcmlrxzYucfxHzjfGS1En4oe1j2-HCTTfD8-4ypC",



import tweepy

oauth2_user_handler = tweepy.OAuth2UserHandler(
    client_id=client_id,
    redirect_uri="https://gokind.xyz/authorize/twitter",
    scope=['tweet.read","users.read'],
    # Client Secret is only necessary if using a confidential client
    #client_secret=client_secret
)


from fastapi import FastAPI, Request
import httpx

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="secret-string")



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
    #redirect_uri = "https://gokind.xyz/authorize/twitter"
    #auth_url = f'''https://twitter.com/i/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=tweet.read%20users.read%20follows.read%20follows.write&state=state&code_challenge=challenge&code_challenge_method=plain'''
    #https://twitter.com/i/oauth2/authorize?response_type=code&client_id=N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ&redirect_uri=https%3A%2F%2Fgokind.xyz%2Fauthorize%2Ftwitter&scope=tweet.read%22%2C%22users.read&state=Ep9dePp0xb6i5XlAjkfXj3wtvNdM8s&code_challenge=uoiBXrbwIGCCSwHKs1HPXi_h8MLLE4YGsdBYDcbHNnA&code_challenge_method=S256
    auth_url = oauth2_user_handler.get_authorization_url()
    print(auth_url)
    return RedirectResponse(url=auth_url)


@app.route("/authorize/twitter")
async def authorize_twitter(data):
    #token = data.query_params['code']
    #resp = await oauth.twitter.get('account/verify_credentials.json', token=token)
    access_token = oauth2_user_handler.fetch_token(
    "Authorization Response URL here"
)
    #user_info = resp.json()
    # Use user_info according to your application's needs
    print(token)
    return token



@app.get('/logout')
async def logout(request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
