# Project: Website Blocker
# Version: 1.0
# Author: Felender Hlungwani
# Description: Application to block website at certain time(08:00am - 16:00)
'''For testing purpose replace hosts_path with hosts_path_tem.
   - on windows machine run the file as administor.
   - on mac/linux run the file as sudo
'''

import time
import platform
from datetime import datetime as dt

# Check the type of machine running and set host path
def machine_type():
    h_path = platform.system()
    if h_path == "Darwin":
        hosts_path="/etc/hosts"
        #hosts_path_tem = "hosts"
    else:
        hosts_path =r"c:\Windows\System32\drivers\etc\hosts"
        #hosts_path_tem = "hosts"

    return hosts_path

# initialise redirect varaible and list of blocked website
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","gmail.com", "www.gmail.com"]

path = machine_type()
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours...")

        # check if the content exist on the host file
        # if the content exist then pass else save the content
        # else delete the content

        with open(path, 'r+') as file:
            content = file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website):
                    file.write(line)
            file.trancate()
        print("Fun Hours...")
    time.sleep(5)

machine_type()
