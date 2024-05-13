def convert(no):
    bn_no = bin(no)
    hx_no = hex(no)
    oc_no = oct(no)
    print(f"Nomor Biner: {bn_no[2:]}\nNomor Heksa: {hx_no[2:]}\nNomor Oktal: {oc_no[2:]}")

print(convert(181743))