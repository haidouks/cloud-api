
from pydantic import BaseModel
from typing import List, Optional


class OUTHealth(BaseModel):
    status: str