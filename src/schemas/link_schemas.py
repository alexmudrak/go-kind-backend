import uuid

from pydantic import BaseModel, ConfigDict


class LinkData(BaseModel):
    name: str | None = None
    beneficiary: str | None = None
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ReadLinkData(LinkData):
    id: uuid.UUID
