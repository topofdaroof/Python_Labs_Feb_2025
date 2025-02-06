#! /usr/bin/env python3
# Author: Eul
# Description: This module contains a collection of calculator functions
"""
    Calc App with basic & advanced functions
"""

import sys
import er_basic
import er_adv

def main():
    menu = """"
            Calculator App
            -----------------
            1. Test Basic
            2. Test Adv
            
    """

    print(menu)
    option = input("Choose 1 or 2: ")
    if option == "1":
        print(f"100 + 50 + 25 + 12.5 = {er_basic.add(100, 50, 25, 12.5)}")
        print(f"100 * 50 * 25 * 12.5 = {er_basic.mul(100, 50, 25, 12.5)}")
    elif option == "2":
        print(f"Modulus of 100 by 45 = {er_adv.mod(100, 45)}")
        print(f"square root of 25 = {er_adv.sqrt(25)}")
    else:
        print("invalid option")

# Namespace TRICK
if __name__ == "__main__":e
    #executes only when run directly as a program
    main()
    sys.exit(0)