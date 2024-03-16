from fastapi import Depends,status, FastAPI, Request, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
import traceback
from fastapi import FastAPI, Depends, HTTPException
from authlib.integrations.starlette_client import OAuth
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

from utils.auth_helper import get_twitter_token, get_twitter_authorize_url_and_verifier, client_id, client_secret

from fastapi import FastAPI, Request
import ssl

#openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

app = FastAPI()


redirect_uri = "https://gokind.xyz"

from tweepy import OAuth2UserHandler

def _oauth2_handler(callback_url: str) -> OAuth2UserHandler:
    return OAuth2UserHandler(
        client_id=MY_TWITTER_KEY,
        redirect_uri=callback_url,
        scope=["offline.access", "users.read", "tweet.read"],
        consumer_secret=MY_TWITTER_SECRET,
    )
handler = _oauth2_handler("https://gokind.xyz/authorize/twitter", None)




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

#https://stackoverflow.com/questions/74649514/how-to-recreate-tweepy-oauth2userhandler-across-web-requests
# Flask route to redirect user to Twitter's authorization page
saved_authorize_url = None

@app.get("/login/twitter")
async def login_twitter():
    # Redirect user to Twitter's OAuth 2.0 authorization page
    #redirect_uri = "https://gokind.xyz/authorize/twitter"
    #auth_url = f'''https://twitter.com/i/oauth2/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=tweet.read%20users.read%20follows.read%20follows.write&state=state&code_challenge=challenge&code_challenge_method=plain'''
    #https://twitter.com/i/oauth2/authorize?response_type=code&client_id=N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ&redirect_uri=https%3A%2F%2Fgokind.xyz%2Fauthorize%2Ftwitter&scope=tweet.read%22%2C%22users.read&state=Ep9dePp0xb6i5XlAjkfXj3wtvNdM8s&code_challenge=uoiBXrbwIGCCSwHKs1HPXi_h8MLLE4YGsdBYDcbHNnA&code_challenge_method=S256
    authorize_url, code_verifier = get_twitter_authorize_url_and_verifier("https://gokind.xyz/authorize/twitter")
    saved_authorize_url = authorize_url
    print(authorize_url, code_verifier)
    #return JSONResponse(content={"authorize_url":authorize_url, "code_verifier":code_verifier }) 
    return RedirectResponse(url=authorize_url)


@app.get("/authorize/twitter")
async def authorize_twitter(state, code, request: Request):

    #twitter_verifier = code
    #result = get_twitter_token(callback_url=saved_authorize_url,
    #                  current_url=str(request.url),
    #                  twitter_verifier=twitter_verifier)
    #return result
    token_data = handler.fetch_token(str(request.url))
    print(token_data) 

import requests
import base64


@app.get("/v2/authorize/twitter")
async def authorize_twitter(state, code, request: Request):
    auth_code = code #"auth_code_from_callback"
    code_verifier = "123" #"code_challenge_string"  # Should match the verifier used to generate the challenge
    
    
# Encode the Client ID and Secret
    client_credentials = f"{client_id}:{client_secret}"
    client_credentials_bytes = client_credentials.encode("ascii")
    base64_encoded_credentials = base64.b64encode(client_credentials_bytes)
    authorization_header_value = base64_encoded_credentials.decode("ascii")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {authorization_header_value}"
    }

    token_url = "https://api.twitter.com/2/oauth2/token"
    data = {
        "code": auth_code,
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code_verifier": code_verifier
    }

    response = requests.post(token_url, data=data, headers=headers)

    # Check the response
    if response.ok:
        tokens = response.json()
        access_token = tokens.get("access_token")
        refresh_token = tokens.get("refresh_token")  # If you requested offline_access
        print("Access Token:", access_token)
    else:
        print("Failed to obtain tokens", response.text)



@app.get('/logout')
async def logout(request):
    request.session.pop('user', None)
    return RedirectResponse(url='/')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_keyfile="key.pem", ssl_certfile="cert.pem")
