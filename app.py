# Project: Website Blocker
# Version: 1.0
# Author: Felender Hlungwani
# Description: Application to block website a certain time

import time
import platform
from datetime import datetime as dt

# Get machine type and set host path
def machine_type():
    h_path = platform.system()
    if h_path == "Darwin":
        #hosts_path="/etc/hosts"
        hosts_path_tem = "hosts"
    else:
        hosts_path=r"c:\Windows\System32\drivers\etc\hosts"
    return

# initialise redirect varaible and list of blocked website
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","gmail.com", "www.gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours...")
        with open(machine_type(), 'r+') as file:
            content.file.read()
            print(content)
    else:
        print("Fun Hours...")
    time.sleep(5)

machine_type()
