NIMS = (23090043,23090002,23090121,23090072,23090092)

i=1
for NIM in NIMS:
    print(f"NIM Biner {i}: {bin(NIM)[2:]}")
    i+=1
    if i==6:
        print("")

i=1
for NIM in NIMS:
    print(f"NIM Heksa {i}: {hex(NIM)[2:]}")
    i+=1
    if i==6:
        print("")

i=1
for NIM in NIMS:
    print(f"NIM Oktal {i}: {oct(NIM)[2:]}")
    i+=1
    if i==6:
        print("")