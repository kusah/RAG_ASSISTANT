from pydantic import BaseModel, ConfigDict
from datetime import datetime


class DocumentResponse(BaseModel):
    id: int
    filename: str
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)