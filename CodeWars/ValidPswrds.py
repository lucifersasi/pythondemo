# You will receive a list of passwords with different conditions attached to them.
# A password is only valid if the specified letter x occurs at least a times and at most b times.
# How many passwords are valid?


# Input
# Line 1: n passwords to check
# Line n: a-b x: password

# Output
# number of valid passwords


# Example

# Input
# 20
# 6-8 s: svsssszslpsp
# 3-4 n: gncn
# 4-8 v: vkvmvdmvhttvvrgvvwv
# 16-18 j: jjjjjjjjjjjjjjjjjf
# 13-15 p: pppppppvppppxxppp
# 3-4 k: bkksggqbtwkkkzqcz
# 8-18 x: qxphxxtczxxxxxrbxxl
# 6-11 c: dccxcccccchrcfdckcsc
# 10-11 c: ccvxccccccccc
# 2-4 f: pszff
# 18-20 z: zzzzzzzzzzwzzzzzzzzj
# 1-7 g: ggggggpggggggg
# 3-5 h: hhhhfhh
# 2-5 x: dxxzxv
# 7-8 s: ssssssss
# 3-9 k: ktkkkkkklkck
# 2-9 r: rzrrrrrrrrrrrr
# 5-9 k: tkrkhkxbvkbkkkkk
# 8-9 n: tnnpbnrns
# 14-15 q: qqqqqqqqqqqqqqqq

# Output - 11


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
k = []
for i in range(n):
    line = input()
    k.append(line.split(" "))

# print(k)
rep = 0
for c in k:
    n = c[2].count(c[1][0])
    n1, n2 = c[0].split("-")
    # print(n1, n2)
    if n >= int(n1) and n <= int(n2):
        rep += 1

    # Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(rep)
