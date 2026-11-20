daftar_nama = []

while True:
    nama = input("Masukkan nama calon anggota: ")
    if nama == "selesai":
        break
    daftar_nama.append(nama)

print("\nHasil Evaluasi:")
for nama in daftar_nama:
    if nama == len(nama) <8 or len(nama) <10  :
        print("Nama '" + nama + "' tidak valid.")

penyusup = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if penyusup in daftar_nama:
    while penyusup in daftar_nama:
        daftar_nama.remove(penyusup)
    print("Nama penyusup berhasil dihapus.")
else:
    print("Nama tidak ditemukan di dalam daftar.")