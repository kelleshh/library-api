from pydantic import BaseModel, ConfigDict, Field

class SBookBase(BaseModel):
    title: str
    author: str
    year: int | None = None
    pages: int | None = Field(None, gt=10)
    is_read: bool = False


class SBookAdd(SBookBase):
    pass

class SBook(SBookBase):
    id: int
    # orm support
    model_config = ConfigDict(from_attributes=True)