import tweepy
from oauthlib.oauth2 import OAuth2Error
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from typing import List

client_id="N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ"
client_secret="JMLkZIaNg-IcmlrxzYucfxHzjfGS1En4oe1j2-HCTTfD8-4ypC"
code_verifier= "123"


class NotTweepyOAuth2UserHandler(OAuth2Session):
    def __init__(
        self, client_id: str, client_secret: str, redirect_uri: str, scope, code_verifier: str
    ):
        super().__init__(client_id, redirect_uri=redirect_uri, scope=scope)
        self.auth = HTTPBasicAuth(client_id, client_secret)
        self.code_verifier = code_verifier or str(self._client.create_code_verifier(128))

    def get_authorization_url(self) -> str:
        url, state_seems_unnecessary = self.authorization_url(
            "https://twitter.com/i/oauth2/authorize",
            code_challenge=self._client.create_code_challenge(self.code_verifier, "S256"),
            code_challenge_method="S256",
        )
        return url

    def fetch_token(self, authorization_response):
        return super().fetch_token(
            "https://api.twitter.com/2/oauth2/token",
            authorization_response=authorization_response,
            auth=self.auth,
            include_client_id=True,
            code_verifier=self.code_verifier,
        )

def _oauth2_handler(callback_url: str, code_verifier: str ):
    return NotTweepyOAuth2UserHandler(
        client_id,
        client_secret,
        callback_url,
        ["offline.access", "users.read", "tweet.read"],
        code_verifier=code_verifier,
    )

def get_twitter_authorize_url_and_verifier(callback_url: str):
    handler = _oauth2_handler(callback_url, code_verifier)
    authorize_url = handler.get_authorization_url()
    # the caller can now store code_verifier somehow
    return authorize_url, handler.code_verifier

def get_twitter_token(callback_url: str, current_url: str, twitter_verifier: str): 
    # then pass twitter_verifier back in here 
    print(f'callback_url {callback_url}')
    handler = _oauth2_handler(callback_url, twitter_verifier)

    try:
        print(f'current_url {current_url}')
        return handler.fetch_token(current_url)
    except OAuth2Error as e:
        raise Exception(e.description) from e
    
    