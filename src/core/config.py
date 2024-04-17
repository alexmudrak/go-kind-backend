import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ATTENTION: Need to move all creds data to `.env`
    # file.
    # TODO: Revoke creds
    # APP Creds
    app_client_id: str = os.getenv(
        "APP_CLIENT_ID", "N1gyR29FUXZuWi1UbGF4UTFIdmo6MTpjaQ"
    )
    app_client_secret: str = os.getenv(
        "APP_CLIENT_SECRET",
        "JMLkZIaNg-IcmlrxzYucfxHzjfGS1En4oe1j2-HCTTfD8-4ypC",
    )
    app_redirect_uri: str = os.getenv(
        "APP_REDIRECT_URI", "https://gokind.xyz/api/v1/twitter/authorize"
    )
    app_scopes: list[str] = ["offline.access", "users.read", "tweet.read"]
    # Static setup
    static_files_path: str = os.getenv("STATIC_FILES_PATH", "./static")
    certificates_path: str = os.getenv(
        "CERTIFICATES_PATH", "./certificates"
    )
    # DB setup
    # TODO: Change to Postgresql
    db_url: str = "sqlite+aiosqlite:///./test.db"

    class Config:
        extra = "allow"
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
