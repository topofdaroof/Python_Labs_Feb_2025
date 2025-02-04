#! /usr/bin/env python3
# Author: Eul
# Description: This script will demo HOWTO repeat a block of
# commands a specific number of times using a COUNTER loop
"""
Docstring:
"""

count = 0 # 1. Initialize Counter
while count < 10: # 2. Test counter
    print(count)
    count += 1 # 4. Increment counter

#Alternatively, we could use a FOR loop plus the built-in
# range(start, stop, step) function.
for num in range(0, 10, 1):
    print(num)