def piknik_or_buku(a, b):
    return not(not a and not b)

def dosen_informatika(a, b):
    return not(not a or not b)

piknik = True
buku = False

L = True
P = True

print(f"Soal A: {piknik_or_buku(piknik,buku)}\nSoal B: {dosen_informatika(L,P)}")