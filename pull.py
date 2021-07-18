import os
import paramiko

while True:
    server = input("enter hostname: ")
    username = input("enter username: ")
    password = input("enter password: ")
    localpath = input("enter local path: ")
    remotepath = input("enter remote path: ")


    ssh = paramiko.SSHClient() 
    ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server, username=username, password=password)
    sftp = ssh.open_sftp()
    sftp.put(localpath, remotepath)
    sftp.close()
    ssh.close()