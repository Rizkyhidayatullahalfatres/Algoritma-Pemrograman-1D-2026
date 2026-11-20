baris = int(input("Masukkan jumlah baris lampu: "))
lampu_per_baris = int(input("Masukkan jumlah lampu pada setiap baris: "))

for i in range(1, baris + 1):
    print(f"Baris {i}:")
    for j in range(1, lampu_per_baris + 1):
        if j % 2 == 0:
            print(f"  Lampu {j}: Mengalami gangguan")
        elif j % 3 == 0: 
            print(f"lampu {j} mengalami error")
        else:
            print(f"  Lampu {j}: Berfungsi normal")

print("Periksa sumber listrik utama taman.")