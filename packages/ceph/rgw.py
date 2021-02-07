import os
from rgwadmin import RGWAdmin

class RGW:
    def __init__(self):
        host = os.getenv("host")
        access_key = os.getenv("access_key")
        secret_key = os.getenv("secret_key")
        self.__rgwAdmin = RGWAdmin(server=host, access_key=access_key, secret_key=secret_key, verify=False)

    @property
    def rgwAdmin(self):
        """Get the RGW client"""
        return self.__rgwAdmin