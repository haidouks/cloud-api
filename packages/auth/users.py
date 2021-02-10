from pydantic import BaseModel
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends,HTTPException,status
import secrets
from typing import Optional
from pprint import pprint

class User(BaseModel):
    userName: str
    role: Optional[str]
    password: str

class UserInventory:
    security = HTTPBasic()
    userDB = {
             "aslan" : {
                 "password": "Aslan12345",
                 "role": "k8s-admin",
             },
             "cansin" : {
                 "password": "Cansin12345",
                 "role": "guest",
             }
         }
    @classmethod
    def checkAuth(cls, credentials: HTTPBasicCredentials = Depends(security)):
        user = cls.getUser(credentials.username)
        if user:
            correct_password = secrets.compare_digest(credentials.password, user.get("password"))
            if correct_password:
              return credentials.username
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    @classmethod
    def getUser(cls,user: str = None):
        if user:
            return cls.userDB.get(user)
        return cls.userDB

    @classmethod
    def getCurrentUser(cls, credentials: HTTPBasicCredentials = Depends(security)):
        user = cls.getUser(credentials.username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Basic"},
            )
        return User(
            userName = credentials.username, password = credentials.password, role= user.get("role")
            )

        