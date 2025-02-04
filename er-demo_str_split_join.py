#! /usr/bin/env python3
# Author: Eul
# Description: This script will demo
"""
Docstring:
"""

# Sample line from /etc/passwd on Linux for the root user login
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# AND I was to MODIFY the string! BUT str are IMMUTABLE!

fields = line.split(":") #Return a LIST - LISTS are MUTABLE!
fields[4] = "The Administrator"
fields[6] = "/bin/bash"
line = ":".join(fields) # Returns a new str object

print(line)
