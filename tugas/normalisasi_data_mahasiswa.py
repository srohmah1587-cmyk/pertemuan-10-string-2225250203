
def normalisasi_nama(nama):
    return " ".join(nama.strip().title().split())


def buat_inisial(nama):
    nama = normalisasi_nama(nama)
    return "".join(kata[0].upper() for kata in nama.split())


def normalisasi_kode(kode):
    return kode.strip().upper()


nama = input("Nama: ")
kode = input("Kode kelas: ")

# Menampilkan hasil normalisasi
print("Nama normalisasi:", normalisasi_nama(nama))
print("Inisial nama:", buat_inisial(nama))
print("Kode kelas normalisasi:", normalisasi_kode(kode))
