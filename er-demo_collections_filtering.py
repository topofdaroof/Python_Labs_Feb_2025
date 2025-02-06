#! /usr/bin/env python3
# Author: Eul
# Description: This script will generate
"""
Docstring:
"""

students = ['euler','george','will','anne','grace']

wee_names = []
for name in students:
    if len(name) <= 5:
        wee_names.append(name)
print(f"1.short names= {wee_names}")

def