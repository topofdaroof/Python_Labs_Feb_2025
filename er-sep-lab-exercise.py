#! /usr/bin/python
#                    1         2         3         4
#          012345678901234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# A line of hyphens the same length as the belgium string
print("-" * len(Belgium))

# the string with the comma separators replaced by colons ':'

bel = Belgium.split(':')

# Belgium = ":".join(bel)

print(Belgium)
print(bel)
print(type(Belgium))


# the population of Belgium (the scond field), plus the population
# of the capital city (the fourth field) answer should be 1183818




# A line of hyphens the same length as the Belgium String