#! /usr/bin/env python3
# Author: Name
# Description: This script will generate
#from
"""
Docstring:
"""

import sys
import re

if sys.platform == "win32":
    filename = r"c:\Windows\System32\drivers\etc\services"
else:
    filename = r"/etc/services"

all_ports = set(range(1,201))
used_ports = set()

with open(filename, mode="rt")as fh_services:
    for line in fh_services:
        m = re.search(r"(\d+)/(tcp|udp)", line)
        if m:
            port = int(m.group(1))
            if port <=200:
                used_ports.add(port)

print(f"All ports = {all_ports}")
print(f"Used ports = {used_ports}")
print(f"Unused ports = {all_ports - used_ports}")