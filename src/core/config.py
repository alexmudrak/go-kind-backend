from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ATTENTION: Need to move all creds data to `.env`
    # file.
    # TODO: Revoke creds
    # APP Creds
    app_client_id: str = "N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ"
    app_client_secret: str = (
        "JMLkZIaNg-IcmlrxzYucfxHzjfGS1En4oe1j2-HCTTfD8-4ypC"
    )
    app_redirect_uri: str = "https://gokind.xyz/api/v1/twitter/authorize"
    app_scopes: list[str] = ["offline.access", "users.read", "tweet.read"]

    class Config:
        extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
