import os
import pysftp
import datetime, threading, time

next_call = time.time()

server = input("enter hostname: ")
username = input("enter username: ")
password = input("enter password: ")
localpath = input("enter local path: ")
remotepath = input("enter remote path: ")



def push():
 with pysftp.Connection(server, username=username, password=password) as sftp:
   with sftp.cd('public'):
     sftp.put(localpath)


def cycle():
 global next_call
 push()
 next_call = next_call+3600

cycle()
