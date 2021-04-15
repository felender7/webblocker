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
        #hosts_path =r"c:\Windows\System32\drivers\etc\hosts"
        hosts_path_tem =r"c:\Windows\System32\drivers\etc\hosts"

    return hosts_path_tem

# initialise redirect varaible and list of blocked website
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","gmail.com", "www.gmail.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours...")

        #Get host path and open/read
        path = machine_type()
        with open(path, 'r+') as file:
            content = file.read()
        # check if the content exist on the host file
        # if the content exist then pass else save the content
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")


    else:
        print("Fun Hours...")
    time.sleep(5)

machine_type()
