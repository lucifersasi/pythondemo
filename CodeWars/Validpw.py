import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
k = []
for i in range(n):
    line = input()
    k.append(line.split(" "))
rep = 0
for c in k:
    dupes = c[2].count(c[1][0])
    min, max = c[0].split("-")
    if dupes >= int(min) and dupes <= int(max):
        rep += 1

print(rep)
