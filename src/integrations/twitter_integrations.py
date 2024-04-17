import tweepy
from requests_oauthlib import OAuth2Session


class TwitterAuthenticator(OAuth2Session):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        scope: list[str],
        access_token: None | str = None,
    ):
        self.user_handler = tweepy.OAuth2UserHandler(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
        )
        self.client = tweepy.Client(access_token) if access_token else None
    def __update_client(self, access_token: str):
        self.client = tweepy.Client(access_token)

    def get_authorization_url(self) -> str:
        return self.user_handler.get_authorization_url()

    def get_access_token(self, url: str) -> dict:
        response = self.user_handler.fetch_token(url)
        access_token = response.get("access_token", None)
        if access_token:
            self.__update_client(access_token)

        return response

    def refresh_user_token(self, refresh_token: str) -> dict:
        response = self.user_handler.refresh_token(
            "https://api.twitter.com/2/oauth2/token",
            refresh_token=refresh_token,
        )
        access_token = response.get("access_token", None)
        if access_token:
            self.__update_client(access_token)

        return response

    def get_user_info(self):
        if not self.client:
            raise

        user = self.client.get_me(user_auth=False)

        return user
