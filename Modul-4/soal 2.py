total_gaji = 0

for hari in range(1, 8):
    print(f"Hari ke-{hari}")
    
    while True:
        shift = input("Apakah bekerja shift malam? (ya/tidak): ").lower()
        if shift == "ya" or shift == "tidak":
            break
        print("Input tidak valid, masukkan 'ya' atau 'tidak'.")
        
    while True:
        jam_lembur = int(input("Masukkan jam lembur: "))
        
        if jam_lembur < 0:
            print("Jam lembur tidak boleh negatif. Silakan masukkan ulang.")
            continue
            
        if jam_lembur > 8:
            print("Jumlah lembur melebihi batas yang ditentukan dan tidak dihitung. Silakan masukkan ulang.")
            continue
            
        if jam_lembur == 5 or jam_lembur == 7:
            print("Jam lembur tidak sesuai ketentuan tarif resmi. Silakan masukkan ulang.")
            continue
            
        break

    gaji_pokok = 100000
    upah_lembur = 0
    
    if 1 <= jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000

    tambahan_malam = 50000 if shift == "ya" else 0
    
    gaji_hari_ini = gaji_pokok + upah_lembur + tambahan_malam
    total_gaji += gaji_hari_ini

print(f"Total gaji mingguan karyawan: Rp{total_gaji}")