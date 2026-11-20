asisten_awal = []
while True:
    nama = input("Masukkan nama asisten awal: ")
    if nama == "cukup":
        break
    if nama != "":
        asisten_awal.append(nama)

wadah_awal_terkunci = tuple(asisten_awal)

daftar_gabungan = list(wadah_awal_terkunci)
while True:
    nama = input("Masukkan nama asisten tambahan: ")
    if nama == "cukup":
        break
    if nama != "":
        daftar_gabungan.append(nama)

wadah_baru = tuple(daftar_gabungan)

hari_tugas = []
while True:
    hari = input("Masukkan hari tugas: ")
    if hari == "cukup":
        break
    if hari != "":
        hari_tugas.append(hari)

except_asisten = input("Masukkan nama asisten yg dikecualikan: ")
except_hari = input("Masukkan hari yg dikecualikan: ")

print("\nKombinasi Shift:")
idx = 0
for hari in hari_tugas:
    if idx >= len(wadah_baru):
        idx = 0
        
    asisten = wadah_baru[idx]
    
    if asisten == except_asisten and hari == except_hari:
        idx += 1
        continue
        
    print("Hari " + hari + ": " + asisten)
    idx += 1