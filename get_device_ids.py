#!/bin/python
from gmusicapi import Mobileclient
import pprint
import config as config


conf = config.config()
working_device_id = conf.get_device_id() 
folder = conf.get_folder()
problem=False #stores if one thing below does not work
problems=[] #stores what went wrong
if folder=="unset":
    problems.append("folder is not set, set to the directory you want to store the music,")
    problem=True
if conf.get_email()=="blahemail":
    problems.append("either username or password is not set")
    problem=True
elif(conf.get_password()=="blahpass"):
    problems.append("either username or password is not set")
    problem=True
if problem:
    print "you must go and edit 'config.cfg' in the main director manually and fix the following things: (this will be fixed in a later version)"
    for Problem in problems:
        print"  "+Problem
    exit(1)
del problem
del problems
del conf
api = Mobileclient()
conf = config.config()
email = conf.get_email()
password = conf.get_password()
pp = pprint.PrettyPrinter(indent=4)


if not api.login(email, password, Mobileclient.FROM_MAC_ADDRESS):
   print("login failed, your username and password are probably not correctly set in config.cfg")
   exit(1)
pp.pprint(api.get_registered_devices())
api.logout()
exit(0)
