from .rgw import RGW
import json
import logging
import os
from datetime import date,timedelta,datetime

class UserOperations(RGW):
    
    level = os.getenv("logLevel") if os.getenv("logLevel") else logging.INFO
    logging.basicConfig(level=level,format="%(asctime)s %(levelname)s %(message)s")
    
    def __init__(self):
        RGW.__init__(self) 

    def getUsers(self):
        userList = []
        users = self.rgwAdmin.get_users()
        for user in users:
            userList.append(user)
        return userList

    def getUser(self, uid):
        user = dict(self.rgwAdmin.get_user(uid=uid,stats=True))
        user['keys'] = "*****"
        return user

    def getCurrentUsage(self, uid: str, reportDate: str, interval: int):
        dateObj = datetime.strptime(reportDate, '%Y%m%d')
        end = (dateObj + timedelta(days = interval)).strftime("%Y-%m-%d %H:%M:%S") 
        start = dateObj.strftime("%Y-%m-%d %H:%M:%S")
        usage = self.rgwAdmin.get_usage(uid=uid,start=start, end=end,show_summary=False,show_entries=True)
        return usage