
def baca_nilai(nama_file):
    with open(nama_file, "r") as file:
        data = file.read()
    return data


print(baca_nilai("nilai.txt"))
