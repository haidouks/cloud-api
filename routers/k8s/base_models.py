
from pydantic import BaseModel
from typing import List, Optional

class MetadataInfo(BaseModel):
    name: str
    uid: str

class Metadata(BaseModel):
    metadata: MetadataInfo
    status: dict

class NamespaceList(BaseModel):
    items: List[Metadata]

class PipelineRunInput(BaseModel):
    pipelineRef: str
    image: str
    gitRepo: str
    namespace: Optional[str] = "default"