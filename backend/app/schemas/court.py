from pydantic import BaseModel


class CourtResponse(BaseModel):
    id: int
    name: str
    surface: str
    indoor: bool
    active: bool

    model_config = {
        "from_attributes": True
    }