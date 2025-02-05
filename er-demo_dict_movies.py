#! /usr/bin/env python3
# Author: Eul
# Description: This script will demo will demo HOWTO create, and grow, and shrink
# dictionaries (unordered collections with UNIQUE keys)
# NOTE: dict are in INSERTION order after Python 3.6
"""
Docstring:
"""
import pprint

movies ={'bob': ['fury', 'pulp fiction', 'shawshank redemption'],
        'alice':['pulp fiction','star wars','LoR'],
        'tom':['juno','mission impossible','blink'],
        'rick':['it','friday the 13th','click'],
}

pprint.pprint(movies)
print("-" * 60)
print(f"bob's favorite films are {movies.get('bob')}")
print(f"bob's ultimate film is {movies['bob']}")
print(f"bob's ultimate film is {movies['bob'][0]}")