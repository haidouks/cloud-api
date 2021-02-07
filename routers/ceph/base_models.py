from pydantic import BaseModel
from typing import List, Optional


class OUTHealth(BaseModel):
    status: str

class Stats(BaseModel):
    size: int
    size_actual: int
    size_utilized: int
    size_kb: int
    size_kb_actual: int
    size_kb_utilized: int
    num_objects: int

class Categories(BaseModel):
    category: str
    bytes_sent: int
    bytes_received: int
    ops: int
    successful_ops: int

class BucketUsage(BaseModel):
    bucket: str
    time: str
    epoch: int
    owner: str
    categories: List[Categories]

class BucketUsageEntries(BaseModel):
    user: str
    buckets: List[BucketUsage]

class OUTStats(BaseModel):
    uid: str
    stats: Stats

class OUTUsage(BaseModel):
    entries: List[BucketUsageEntries]

class OUTUids(BaseModel):
    uids: List[str]