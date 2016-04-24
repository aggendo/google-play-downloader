import ConfigParser #TODO: this is renamed in python 3 so use try statement
import os
from os.path import join, exists
import logging
import os

#example format:
"""
***REMOVED***
....
***REMOVED***
email=myEmail
password=myPassword
deviceid=myDeviceId
folder=myFolder

***REMOVED***
settingsversion=1
"""

class Config:

    def __init__(self, path=None):
        if not path==None:
            path = os.path.join(path, 'config.cfg') #custom config dir
        else:
            self.path = 'config.cfg'
        self.config = ConfigParser.ConfigParser()
        if not os.path.exists(self.path):
            logging.debug("generating config file")
            self.generate_cfg()
        self.config.readfp(open(self.path))

    def get_password(self):
        return(self.config.get("Credentials", "password"))

    def get_email(self):
        return(self.config.get("Credentials", "email"))

    def get_device_id(self):
        return(self.config.get("Credentials", "deviceid")) #has a unit at the end so no int

    def set_password(self, pas):
        self.config.set("Credentials", "password", pas)
        self.write_out()
        

    def set_email(self, email):
        self.config.set("Credentials", "email", email)
        self.write_out()

    def set_device_id(self, devId):
        self.config.set("Credentials", "deviceid", devId)
        self.write_out()

    def get_folder(self):
        return(self.config.get("Settings", "folder"))

    def set_folder(self, folder):
        self.config.set("Settings", "folder", folder)
        self.write_out()

    def write_out(self):
        self.config.write(open(self.path, "w"))
    
    def generate_cfg(self):
        self.config.add_section("Credentials")
        self.config.set("Credentials", "email", "blahemail")
        self.config.set("Credentials", "password", "blahpass")
        self.config.set("Credentials", "deviceid", "blahid")
        self.config.add_section("Settings")
        self.config.set("Settings", "folder", "unset")
        self.config.add_section("Info")
        self.config.set("Info", "settingsversion", "1")
        self.write_out()
if __name__=="__main__":
    d = config()
def config(path=None):
    return(Config(path=path))
