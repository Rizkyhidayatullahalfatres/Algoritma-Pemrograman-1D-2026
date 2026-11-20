data_beasiswa = []
kuota_penuh = 0

print("PROGRAM SELEKSI AWAL BEASISWA")

for i in range(1, 11):
    if kuota_penuh >= 3:
        print("\nProses dihentikan karena kuota beasiswa penuh sudah terpenuhi (3 mahasiswa).")
        break
        
    print(f"\nData Mahasiswa ke-{i}")
    nama = input("Nama: ")
    ipk = float(input("IPK: "))
    
    if ipk < 3.00:
        print("IPK kurang dari 3.00, mahasiswa tidak memenuhi syarat.")
        continue
        
    gaji = float(input("Penghasilan Orang Tua per bulan: Rp"))
    
    if gaji <= 3000000:
        status = "Beasiswa Penuh"
        kuota_penuh += 1
    elif 3000000 < gaji <= 5000000:
        status = "Beasiswa Sebagian"
    else:
        status = "Tidak Mendapatkan Beasiswa"
        
    mahasiswa = {
        "nama": nama,
        "ipk": ipk,
        "gaji": gaji,
        "status": status
    }
    data_beasiswa.append(mahasiswa)

print("\nHASIL SELEKSI BEASISWA")
print(f"{'Nama':<15} {'IPK':<6} {'Penghasilan':<15} {'Status Kelulusan':<25}")

for mhs in data_beasiswa:
    print(f"{mhs['nama']:<15} {mhs['ipk']:<6.2f} Rp{mhs['gaji']:<13,.0f} {mhs['status']:<25}")