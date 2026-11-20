 tugas = {}

while True:
    print("\nMenu:")
    print("1. Tambah tugas")
    print("2. Lihat semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Jumlah tugas selesai dan belum")
    print("6. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama tugas: ")
        tugas[nama] = "Belum selesai"
        print("Tugas ditambahkan")

    elif pilih == "2":
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            for k, v in tugas.items():
                print(k, "-", v)

    elif pilih == "3":
        nama = input("Nama tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Status tugas diubah")
        else:
            print("Tugas tidak ditemukan")

    elif pilih == "4":
        nama = input("Nama tugas yang dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print("Tugas dihapus")
        else:
            print("Tugas tidak ditemukan")

    elif pilih == "5":
        selesai = 0
        belum = 0
        for status in tugas.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1
        print("Selesai:", selesai)
        print("Belum selesai:", belum)

    elif pilih == "6":
        break

    else:
        print("Menu tidak ada")