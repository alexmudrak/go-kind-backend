import tweepy
from requests_oauthlib import OAuth2Session



class TwitterAuthenticator(OAuth2Session):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        scope: list[str],
    ):
        self.user_handler = tweepy.OAuth2UserHandler(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
        )

    def get_authorization_url(self) -> str:
        return self.user_handler.get_authorization_url()

    def get_access_token(self, url: str) -> dict:
        return self.user_handler.fetch_token(url)
