
def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


test_nilai = [59, 60, 61, 75]

for nilai in test_nilai:
    print(nilai, "=", status_lulus(nilai))
