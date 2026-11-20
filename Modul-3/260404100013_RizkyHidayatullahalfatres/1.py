jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

print("Program Kasir Bus Terminal Sidoarjo")

while True:
    jarak = float(input("Masukkan jarak penumpang ke-{jumlah_penumpang + 1}: "))
    
    if jarak == 0:
        break
        
    if jarak < 0:
        print("Jarak tidak valid! Masukkan angka positif.")
        continue

    jumlah_penumpang += 1
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
        
    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500
        
    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 0.5
        print(f"-> Penumpang ke-{jumlah_penumpang} mendapat diskon 50%!")
        
    total_pendapatan += tarif

print("Laporan Akhir")
print(f"Jumlah Penumpang : {jumlah_penumpang} orang")
print(f"Total Pendapatan : Rp{total_pendapatan:,.0f}")
print(f"Jarak Terjauh    : {jarak_terjauh} km")

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print(f"Rata-rata Jarak  : {rata_rata:.2f} km")
else:
    print("Rata-rata Jarak  : 0 km")