from fastapi import Depends,HTTPException,status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from typing import List
from pprint import pprint
from .users import User,UserInventory

class RoleChecker:

    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(UserInventory.getCurrentUser)):
        if user.role not in self.allowed_roles:
            pprint(f"Route requires {self.allowed_roles} role but User({user.userName}) has {user.role}")
            raise HTTPException(status_code=403, detail="Operation not permitted")
