import pysftp
import yaml

config = "config.yml"

with open(config, "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

for section in cfg:
 server = cfg["main"]["server"]
 username = cfg["main"]["username"]
 password = cfg["main"]["password"]
 remotepath = cfg["main"]["remotepath"]
 localpath = cfg["main"]["localpath"]
 print("Loaded config ---> "+config) 
 print("Loaded server ---> "+server)
 print("Loaded username ---> "+username)
 print("Loaded remotepath ---> "+remotepath)
 print("Loaded save path ---> "+localpath) 


 sftp = pysftp.Connection(server, username=username, password=password)
 if remotepath == "NOAA18":
   sftp.get_r("/home/pi/AltiWx/data/NOAA-18/", localpath, preserve_mtime=True)
 elif remotepath == "NOAA15":
   sftp.get_r("/home/pi/AltiWx/data/NOAA-15/", localpath, preserve_mtime=True)
 elif remotepath == "METEOR-M2":
   sftp.get_r("/home/pi/AltiWx/data/METEOR-M2/", localpath, preserve_mtime=True)
 elif remotepath == "NOAA19":
   sftp.get_r("/home/pi/AltiWx/data/NOAA-19/", localpath, preserve_mtime=True)
 elif remotepath == "ALL":
   sftp.get_r("/home/pi/AltiWx/data/", localpath , preserve_mtime=True)
 elif remotepath == "userinput":
   userinput = remotepath
   sftp.get_r(userinput, localpath, preserve_mtime=True)

