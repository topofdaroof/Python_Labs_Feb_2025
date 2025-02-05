#! /usr/bin/env python3
# Author: Name
# Description: This script will generate
"""
Docstring:
"""
import re
#Open file handle for READING in TEXT mode
fh_in = open(r"c:\labs\postcodes.txt", mode ="rt")
#ITERATE through file hanlde one line at a time
for postcode in fh_in:
    if postcode.isspace(): continue
    #

