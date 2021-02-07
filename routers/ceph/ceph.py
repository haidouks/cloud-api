from .base_models import *
from packages.ceph.ceph import UserOperations
from pprint import pprint
from fastapi import APIRouter, Path, Query, Depends, HTTPException,status
from typing import Optional
from datetime import datetime

router = APIRouter()  
uo = UserOperations()

@router.get("/ceph/users",response_model=OUTUids, tags=["ceph"])
def list_users():
  return {"uids": uo.getUsers()}

@router.get("/ceph/users/{uid}/stats", response_model=OUTStats, tags=["ceph"])
def get_stats_for_uid(uid: str = Path(..., description="The ID of the user")):
  result = {
    "uid" : uid,
    "stats" : uo.getUser(uid)["stats"],
  }
  return result

@router.get("/ceph/users/{uid}/usage", response_model=OUTUsage, tags=["ceph"])
def get_usage_for_uid(uid: str = Path(..., description="The ID of the user"),
                            reportDate: Optional[str] = Query(datetime.now().strftime("%Y%m%d"), description="Report date in YYYYMMDD", regex="^(?:(?:(?:(?:(?:[13579][26]|[2468][048])00)|(?:[0-9]{2}(?:(?:[13579][26])|(?:[2468][048]|0[48]))))(?:(?:(?:09|04|06|11)(?:0[1-9]|1[0-9]|2[0-9]|30))|(?:(?:01|03|05|07|08|10|12)(?:0[1-9]|1[0-9]|2[0-9]|3[01]))|(?:02(?:0[1-9]|1[0-9]|2[0-9]))))|(?:[0-9]{4}(?:(?:(?:09|04|06|11)(?:0[1-9]|1[0-9]|2[0-9]|30))|(?:(?:01|03|05|07|08|10|12)(?:0[1-9]|1[0-9]|2[0-9]|3[01]))|(?:02(?:[01][0-9]|2[0-8])))))$"),
                            interval: Optional[int] = Query(1,description="Interval for the report in days")):
  return uo.getCurrentUsage(uid=uid,reportDate=reportDate,interval=interval)