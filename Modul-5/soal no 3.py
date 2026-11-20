def hitung_nilai(nama, tugas, uts, uas):
    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 55:
        grade = "C"
    else:
        grade = "D"
        
    if grade == "A" or grade == "B" or grade == "C":
        status = "Lulus"
    else:
        status = "Tidak Lulus"
        
    print("\n HASIL PERHITUNGAN")
    print(f"Nama Mahasiswa: {nama}")
    print(f"Nilai Akhir   : {nilai_akhir}")
    print(f"Grade         : {grade}")
    print(f"Status        : {status}")

nama_mhs = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

hitung_nilai(nama_mhs, nilai_tugas, nilai_uts, nilai_uas)