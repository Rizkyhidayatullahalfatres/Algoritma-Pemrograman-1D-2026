playlist = {}

while True:
    print("\nMenu:")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        nama = input("Nama playlist: ")
        if nama not in playlist:
            playlist[nama] = {}
            print("Playlist dibuat")
        else:
            print("Playlist sudah ada")

    elif pilih == "2":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu: ")
            penyanyi = input("Penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("Lagu ditambahkan")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "3":
        if len(playlist) == 0:
            print("Playlist masih kosong")
        else:
            for p, lagu in playlist.items():
                print("Playlist:", p)
                for j, art in lagu.items():
                    print(" -", j, "(", art, ")")

    elif pilih == "4":
        cari = input("Judul lagu yang dicari: ")
        ada = False
        for p, lagu in playlist.items():
            if cari in lagu:
                print("Ditemukan di", p, ":", cari, "-", lagu[cari])
                ada = True
        if not ada:
            print("Lagu tidak ditemukan")

    elif pilih == "5":
        nama = input("Nama playlist: ")
        if nama in playlist:
            judul = input("Judul lagu yang dihapus: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu dihapus")
            else:
                print("Lagu tidak ada di playlist")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "6":
        nama = input("Nama playlist yang dihapus: ")
        if nama in playlist:
            del playlist[nama]
            print("Playlist dihapus")
        else:
            print("Playlist tidak ditemukan")

    elif pilih == "7":
        break

    else:
        print("Menu tidak tersedia")