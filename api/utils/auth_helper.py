import tweepy
from requests_oauthlib import OAuth2Session

app_client_id = "N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ"
app_client_secret = "JMLkZIaNg-IcmlrxzYucfxHzjfGS1En4oe1j2-HCTTfD8-4ypC"
app_redirect_uri = "https://gokind.xyz/authorize/twitter"
app_scopes = ["offline.access", "users.read", "tweet.read"]


class TwitterWrapper(OAuth2Session):
    def __init__(
        self,
    ):
        self.user_handler = tweepy.OAuth2UserHandler(
            client_id=app_client_id,
            client_secret=app_client_secret,
            redirect_uri=app_redirect_uri,
            scope=app_scopes,
        )

    def get_authorization_url(self) -> str:
        return self.user_handler.get_authorization_url()

    def get_access_token(self, url: str) -> dict:
        return self.user_handler.fetch_token(url)
