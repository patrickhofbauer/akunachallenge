import math
import fractions
from itertools import permutations

STONE_NUMS = 7
LEFT_NUM = 1

valid_sequences = []
perms = permutations([i for i in range(2, STONE_NUMS+1)])

for perm in perms:
    left_jumps = LEFT_NUM-1
    for i in range(5):
        if perm[i] > perm[i+1]:
            left_jumps += 1

    if left_jumps == LEFT_NUM:
        valid_sequences.append(perm)

print("Probability: " + str(fractions.Fraction(len(valid_sequences), math.factorial(STONE_NUMS-1))))
#Answer: 19/240
