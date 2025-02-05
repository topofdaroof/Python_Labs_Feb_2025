#! /usr/bin/env python3
# Author: Eul
# Description: This script will simulate a high street bank
"""
Docstring:
"""


master_pin = "0123"
pin = None
attempts = 0

# Loop whilst PIN is incorrect

while pin != master_pin and attempts < 3:
    pin = input("Enter Pin: ")
    if pin == master_pin:
        print("Valid Pin")
        continue
        break
    else:
        print("Invalid Pin")
        attempts += 1

print("done")
print(leave)
