import random

NIMS = (23090043,23090002,23090121,23090072,23090092)
NIMSET = list(NIMS)
def random3digit():
    return random.randint(0, 999)

for i in range(len(NIMSET)):
    Digit_Baru = random3digit()

    NIMSET[i] = (NIMSET[i] - (NIMSET[i] % 1000)) + Digit_Baru

print(tuple(NIMSET))