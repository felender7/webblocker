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
    else:
        hosts_path=r"c:\Windows\System32\drivers\etc\hosts"
    return

redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","gmail.com", "www.gmail.com"]
machine_type()
