data_mahasiswa = []
jumlah_A = jumlah_B = jumlah_C = jumlah_D = jumlah_E = 0
total_nilai_kelas = 0

print("--- Program Pengelolaan Nilai Mahasiswa ---")

for i in range(1, 11):
    print(f"\nMasukkan data Mahasiswa ke-{i}:")
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    total_nilai_kelas += nilai_akhir
    
    if 85 <= nilai_akhir <= 100:
        kategori = "A"
        jumlah_A += 1
    elif 75 <= nilai_akhir < 85:
        kategori = "B"
        jumlah_B += 1
    elif 65 <= nilai_akhir < 75:
        kategori = "C"
        jumlah_C += 1
    elif 50 <= nilai_akhir < 65:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1
        
    mahasiswa = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": nilai_akhir,
        "kategori": kategori
    }
    data_mahasiswa.append(mahasiswa)

tertinggi = data_mahasiswa[0]
terendah = data_mahasiswa[0]

print("\nDATA NILAI MAHASISWA")
print(f"{'Nama':<15} | {'Tugas':<6} | {'UTS':<6} | {'UAS':<6} | {'Nilai Akhir':<11} | {'Kategori':<8}")
print("-" * 65)

for mhs in data_mahasiswa:
    print(f"{mhs['nama']:<15} | {mhs['tugas']:<6.1f} | {mhs['uts']:<6.1f} | {mhs['uas']:<6.1f} | {mhs['akhir']:<11.2f} | {mhs['kategori']:<8}")
    
    if mhs['akhir'] > tertinggi['akhir']:
        tertinggi = mhs
        
    if mhs['akhir'] < terendah['akhir']:
        terendah = mhs

print("\nLAPORAN AKHIR")
print(f"Jumlah Kategori A : {jumlah_A} mahasiswa")
print(f"Jumlah Kategori B : {jumlah_B} mahasiswa")
print(f"Jumlah Kategori C : {jumlah_C} mahasiswa")
print(f"Jumlah Kategori D : {jumlah_D} mahasiswa")
print(f"Jumlah Kategori E : {jumlah_E} mahasiswa")
print("-" * 60)
print(f"Nilai Tertinggi   : {tertinggi['akhir']:.2f} ({tertinggi['nama']})")
print(f"Nilai Terendah    : {terendah['akhir']:.2f} ({terendah['nama']})")
print(f"Rata-rata Kelas   : {total_nilai_kelas / 10:.2f}")