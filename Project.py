def cek_kategori_tinggi(gender, tinggi):
    # Standar rata-rata tinggi badan di Indonesia (pendekatan umum)
    if gender == "L":
        if tinggi < 160:
            return "Kurang"
        elif 160 <= tinggi <= 175:
            return "Ideal / Normal"
        else:
            return "Tinggi"
    elif gender == "P":
        if tinggi < 150:
            return "Kurang"
        elif 150 <= tinggi <= 165:
            return "Ideal / Normal"
        else:
            return "Tinggi"
    else:
        return "Gender tidak valid"

def main():
    print("=== PROGRAM PENGECEK KATEGORI TINGGI BADAN ===")
    
    # Input Jenis Kelamin
    print("\nPilih Jenis Kelamin:")
    print("L = Laki-laki")
    print("P = Perempuan")
    gender = input("Masukkan pilihan (L/P): ").upper().strip()
    
    if gender not in ["L", "P"]:
        print("Error: Pilihan jenis kelamin salah!")
        return

    # Input Tinggi Badan dengan Validasi Angka
    try:
        tinggi = float(input("Masukkan tinggi badan Anda (dalam cm): "))
        if tinggi <= 0:
            print("Error: Tinggi badan harus lebih dari 0!")
            return
            
        # Proses Cek Kategori
        kategori = cek_kategori_tinggi(gender, tinggi)
        
        # Tampilkan Hasil
        print("\n--- HASIL ANALISIS ---")
        print(f"Jenis Kelamin : {'Laki-laki' if gender == 'L' else 'Perempuan'}")
        print(f"Tinggi Badan  : {tinggi} cm")
        print(f"Kategori      : {kategori}")
        
    except ValueError:
        print("Error: Mohon masukkan angka yang valid untuk tinggi badan!")

if __name__ == "__main__":
    main()